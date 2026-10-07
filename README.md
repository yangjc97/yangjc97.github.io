# Jichang Yang’s academic website

Personal academic homepage at https://yangjc97.github.io, using the official **al-folio v1** runtime (`al_folio_core` 1.0.15).

## Preview locally

Use Ruby 3.3 or newer. On macOS, put your Homebrew Ruby `bin` directory ahead of the system Ruby in `PATH`.

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
```

Open http://localhost:4000. Restart the server after editing `_config.yml`.

Alternatively, with Docker installed:

```sh
docker compose up --build
```

## Edit content

| Content | Location |
| --- | --- |
| Biography and homepage | `_pages/about.md` |
| Publication records and abstracts | `_publications/*.md` |
| Conference and seminar records (shown on About) | `_talks/*.md` |
| Teaching records (shown on About) | `_teaching/*.md` |
| News (month-level dates) | `_news/*.md` |
| Education | `_data/education.yml` |
| Email and Scholar | `_data/socials.yml` |
| CV PDF path and last update date | `_data/cv.yml` |
| Identity, hosting and feature settings | `_config.yml` |
| Portrait, university logos and favicon | `assets/img/` |
| Small visual customizations | `_sass/_site.scss` |

Published papers are grouped by year, newest first. Within each year, `year_priority` sets the display order (smaller numbers first): first-listed and equal-contribution papers come first, ordered by Jichang Yang’s author position; ties retain the preferred IEDM order or use venue priority. Other co-authored papers use an editorial venue order, with author position as a tie-breaker. The current co-author preferences are Science Advances before Cyborg and Bionic Systems, and IEEE Transactions on Power Electronics before IEEE Transactions on Magnetics. New records without `year_priority` follow the explicitly ordered papers, newest first. `selected: true` and `selected_order` control homepage highlights. Author lists retain the original equal-contribution and corresponding-author marks. Set `published: false` to keep a manuscript out of the generated website. Liquid comment blocks continue to protect withheld abstracts. Individual publication and teaching pages are disabled; the records remain as data for the lists. The old Talks, Teaching and News page URLs redirect to the matching About sections.

This site deliberately keeps Markdown publication records instead of adding a second BibTeX database and Jekyll Scholar dependency. Shared layouts, styles, navigation and dark mode come from the official al-folio gem. The site defaults to light mode on first visit, retains saved theme choices, and keeps the theme toggle available. Site-owned overrides are limited to content snippets, the base page layout (removing the unused bibliography tag), `main.scss` (adding the custom style import), and `assets/js/theme.js` (changing the initial theme from system to light). The overrides were based on core 1.0.15; review them when updating the core gem.

## Publication images

Place paper figures in `assets/img/publications/`. Add these optional fields to the YAML header of the corresponding `_publications/*.md` file:

```yaml
preview: /assets/img/publications/diffusion.webp
preview_alt: RRAM-based neural differential equation solver architecture
```

`preview` adds a thumbnail to both the homepage highlights and the full publication list, without creating individual paper pages. `preview_alt` describes the image for accessibility; it defaults to the paper title. There are no abstract or detail pages; titles and Paper links point to the external publication when a link is available. Homepage highlights reserve a blank image slot until `preview` is supplied; papers without `preview` in the full publication list stay text-only. Desktop uses an image beside the text; mobile places it above the text. Figures are contained without cropping.

Use a chip photo, a system diagram or a representative result figure. PNG, JPEG, WebP and GIF are supported. Around 800–1200 pixels wide is sufficient for most figures.

## Three-page navigation and CV

The main navigation is **About → Publications → CV**. About includes biography, a scrollable news panel above the highlights, education, talks and teaching. News entries use `emoji` and can set `date_label` when only a year is known. Paper announcements record `author_role` and use a short research topic instead of the full title, followed by the role in parentheses. The first-listed author is shown as First author; other equal-contribution authors as Co-first author; other collaborators as Co-author. The biography lists the Department of Electrical and Computer Engineering, HKU as the primary postdoctoral affiliation, with CASIC, HKU as the secondary affiliation. Contact details are directly below the portrait. Teaching records specify `academic_year` and `semester`; the 2023–2024 Spring course is marked `award: Awarded Best TA`. Publications contains all public papers with external links, without abstract/detail pages.

CV embeds the original PDF in the browser’s PDF viewer, so all document pages are available. It provides Download PDF and an open-in-new-tab fallback for browsers that do not support embedded PDFs.

The CV sources live in the separate sibling `../CV/` directory. `CV_full.pdf` includes manuscripts under review; `CV_public.pdf` omits them. Both are built from `CV_content.tex` and `publications.bib`.

To rebuild both versions and synchronize only the public PDF to this website:

```sh
python3 ../CV/build.py --sync
```

The public PDF is stored at `assets/pdf/CV_public.pdf`; `_data/cv.yml` records its path and update date. The superseded PDF has been removed; only the public CV is included in the website.

## Build and verify

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
python3 scripts/check_site.py
```

Commit `Gemfile.lock` to keep builds reproducible. Update the pinned core version intentionally and preview the site after dependency updates.

## GitHub Pages

The workflow builds on pushes to `main`/`master`, validates local links and hidden content, and deploys the generated artifact. Pull requests build and validate without deploying.

**One-time setting:** In the repository’s **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. GitHub’s default branch-based Jekyll builder does not support this theme’s custom gems.

The sitemap is generated at `/sitemap.xml`, and `/robots.txt` advertises it. For Google Search Console verification, set `google_site_verification` and `enable_google_verification: true`, then submit the sitemap and inspect the homepage URL. These settings help discovery; they do not guarantee indexing.

## Migration and attribution

Migrated from Academic Pages to [al-folio](https://github.com/alshedivat/al-folio). Removed sample attachments, comments, generator examples, unused CV tooling, copied theme internals and the large Plotly bundle. The old visitor-map embed was removed from the homepage. Personal content remains in the existing collections; the Git history retains the previous implementation.

al-folio is MIT licensed. The former Academic Pages license is retained in `LICENSE` for attribution.
