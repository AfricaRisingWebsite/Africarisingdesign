const header = document.querySelector('[data-header]');
const menuToggle = document.querySelector('[data-menu-toggle]');
const menu = document.querySelector('[data-menu]');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function updateHeader() {
  header?.classList.toggle('is-scrolled', window.scrollY > 24);
}

function setMenu(open) {
  if (!header || !menuToggle) return;
  header.classList.toggle('is-open', open);
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.querySelector('.sr-only').textContent = open ? 'Close navigation' : 'Open navigation';
  document.body.classList.toggle('menu-open', open);
  if (open) menu?.querySelector('a')?.focus();
}

updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });
menuToggle?.addEventListener('click', () => setMenu(menuToggle.getAttribute('aria-expanded') !== 'true'));
menu?.addEventListener('click', event => {
  if (event.target.closest('a')) setMenu(false);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuToggle?.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    menuToggle.focus();
  }
});
window.addEventListener('resize', () => {
  if (window.innerWidth > 820 && menuToggle?.getAttribute('aria-expanded') === 'true') setMenu(false);
});

document.querySelectorAll('[data-placeholder-link]').forEach(link => {
  link.addEventListener('click', event => event.preventDefault());
});

const year = document.querySelector('[data-year]');
if (year) year.textContent = new Date().getFullYear();

const revealItems = document.querySelectorAll('.reveal');
if (prefersReducedMotion || !('IntersectionObserver' in window)) {
  revealItems.forEach(item => item.classList.add('is-visible'));
} else {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px' });
  revealItems.forEach(item => observer.observe(item));
}
