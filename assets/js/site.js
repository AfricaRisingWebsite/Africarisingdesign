/* Africa Rising Investments — progressive enhancement only.
   Everything below is optional: the site is fully usable without it. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. Header state on scroll ---- */
  var header = document.querySelector('[data-header]');
  if (header && header.getAttribute('data-solid') !== 'true') {
    var ticking = false;
    var setState = function () {
      header.setAttribute('data-scrolled', window.scrollY > 24 ? 'true' : 'false');
      ticking = false;
    };
    setState();
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(setState); ticking = true; }
    }, { passive: true });
  }

  /* ---- 2. Mobile navigation ---- */
  var toggle = document.querySelector('[data-menu-toggle]');
  var nav = document.querySelector('[data-menu]');
  var scrim = document.querySelector('[data-scrim]');
  var lastFocus = null;

  function focusables() {
    return Array.prototype.filter.call(
      nav.querySelectorAll('a[href], button:not([disabled])'),
      function (el) { return el.offsetParent !== null; }
    );
  }

  function openMenu() {
    lastFocus = document.activeElement;
    nav.setAttribute('data-open', 'true');
    toggle.setAttribute('aria-expanded', 'true');
    if (scrim) scrim.setAttribute('data-open', 'true');
    document.body.classList.add('is-locked');
    var f = focusables();
    if (f.length) f[0].focus();
  }

  function closeMenu() {
    nav.setAttribute('data-open', 'false');
    toggle.setAttribute('aria-expanded', 'false');
    if (scrim) scrim.setAttribute('data-open', 'false');
    document.body.classList.remove('is-locked');
    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.getAttribute('aria-expanded') === 'true' ? closeMenu() : openMenu();
    });
    if (scrim) scrim.addEventListener('click', closeMenu);

    document.addEventListener('keydown', function (e) {
      if (toggle.getAttribute('aria-expanded') !== 'true') return;
      if (e.key === 'Escape') { e.preventDefault(); closeMenu(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && window.matchMedia('(max-width: 60em)').matches) closeMenu();
    });

    window.addEventListener('resize', function () {
      if (!window.matchMedia('(max-width: 60em)').matches &&
          toggle.getAttribute('aria-expanded') === 'true') closeMenu();
    });
  }

  /* ---- 3. Section reveals ---- */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(reveals, function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry, i) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var delay = Math.min(i * 60, 240);
          setTimeout(function () { el.classList.add('is-visible'); }, delay);
          io.unobserve(el);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      Array.prototype.forEach.call(reveals, function (el) { io.observe(el); });
    }
  }

  /* ---- 4. Footer year ---- */
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
