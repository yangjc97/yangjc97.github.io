document.querySelectorAll('.section-dropdown').forEach((item) => {
  const button = item.querySelector('.section-menu-toggle');
  const menu = item.querySelector('.section-menu');
  const setOpen = (open) => {
    menu.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
  };
  item.addEventListener('mouseenter', () => {
    if (window.matchMedia('(hover: hover)').matches) setOpen(true);
  });
  item.addEventListener('mouseleave', () => {
    if (!item.contains(document.activeElement)) setOpen(false);
  });
  button.addEventListener('click', () => setOpen(menu.hidden));
  item.addEventListener('focusout', (event) => {
    if (!item.contains(event.relatedTarget)) setOpen(false);
  });
  item.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') { setOpen(false); button.focus(); }
  });
  menu.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  document.addEventListener('click', (event) => {
    if (!item.contains(event.target)) setOpen(false);
  });
});
