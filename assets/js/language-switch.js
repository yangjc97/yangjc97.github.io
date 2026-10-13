// Keep section links when switching between matching language pages.
document.querySelectorAll('[data-language-switch]').forEach((link) => {
  const update = () => {
    const target = new URL(link.href);
    target.hash = window.location.hash;
    link.href = target.href;
  };
  update();
  window.addEventListener('hashchange', update);
});
