"""Validate built pages, local links and deliberately unpublished content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.urls.append(value)

errors = []
cv_hidden = "published: false" in Path("_pages/cv.html").read_text().split("---")[1]
if cv_hidden:
    for hidden_path in ("cv", "cv.html", "assets/pdf/CV_public.pdf"):
        if (root / hidden_path).exists():
            errors.append(f"Hidden CV content was published: {hidden_path}")
    if "/cv/" in (root / "sitemap.xml").read_text():
        errors.append("Hidden CV page remains in sitemap")
elif not (root / "cv/index.html").is_file():
    errors.append("Missing cv/index.html")
for private_file in ("CV_full.pdf", "CV_content.tex", "CV_full.tex", "CV_latex", "Curriculum_Vitae___Jichang_Yang-2.pdf"):
    if any(root.rglob(private_file)):
        errors.append(f"Private or superseded CV content copied into website: {private_file}")
for required in ("index.html", "publications/index.html", "404.html", "sitemap.xml", "robots.txt", "assets/css/main.css", "assets/css/tailwind.css"):
    if not (root / required).is_file():
        errors.append(f"Missing {required}")
if (root / "publication").exists() or (root / "publications" / "2-IEDM-2024").exists():
    errors.append("Individual publication pages should not be generated")
for page in root.rglob("*.html"):
    parser = Links()
    text = page.read_text()
    parser.feed(text)
    if "/publication/" in text:
        errors.append(f"{page.relative_to(root)}: old publication detail link remains")
    if "{{" in text or "{%" in text:
        errors.append(f"{page.relative_to(root)}: unresolved template markup")
    for url in parser.urls:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        path = unquote(parts.path)
        if cv_hidden and (path.rstrip("/") in ("/cv", "/cv.html") or path == "/assets/pdf/CV_public.pdf"):
            errors.append(f"{page.relative_to(root)}: hidden CV link remains {url}")
        target = root / path.lstrip("/") if path.startswith("/") else page.parent / path
        if not target.exists() and not target.with_suffix(".html").exists():
            errors.append(f"{page.relative_to(root)}: broken link {url}")
    # Hidden submissions and embargoed conference abstract must stay out of generated HTML.
    for withheld in ("Transcending resistive memory noise constraints", "Resistive Memory based Efficient Machine Unlearning", "Efficient lattice field theory simulation", "3.8% accuracy drop"):
        if withheld in text:
            errors.append(f"{page.relative_to(root)}: unpublished content leaked")
    if "main.min.js" in text or "plotly.min.js" in text:
        errors.append(f"{page.relative_to(root)}: old JavaScript bundle remains")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated {len(list(root.rglob('*.html')))} HTML pages, local assets, sitemap and unpublished-content boundaries.")
