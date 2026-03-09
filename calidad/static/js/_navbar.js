// ── Hamburger toggle ──
const hamburger = document.getElementById('hamburger');
const navMenu   = document.getElementById('nav-menu');
const mobileHdr = document.querySelector('.nav-mobile-header');

function isMobile() { return window.innerWidth <= 900; }

function syncMobileHeader() {
  mobileHdr.style.display = isMobile() ? 'flex' : 'none';
}

syncMobileHeader();
window.addEventListener('resize', syncMobileHeader);

hamburger.addEventListener('click', () => {
  navMenu.classList.toggle('open');
  hamburger.innerHTML = navMenu.classList.contains('open')
    ? '<i class="bi bi-x-lg"></i>'
    : '<i class="bi bi-list"></i>';
});

// ── Mobile: toggle dropdowns on click ──
document.querySelectorAll('[data-toggle="dropdown"]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!isMobile()) return;
    e.stopPropagation();
    const dd = btn.nextElementSibling;
    dd.classList.toggle('open');
  });
});

document.querySelectorAll('[data-toggle="submenu"]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!isMobile()) return;
    e.stopPropagation();
    const sm = btn.nextElementSibling;
    sm.classList.toggle('open');
  });
});

// ── Cerrar menú al hacer click fuera ──
document.addEventListener('click', e => {
  if (!e.target.closest('.site-nav')) {
    document.querySelectorAll('.dropdown-menu-custom.open, .submenu.open')
      .forEach(el => el.classList.remove('open'));
  }
});
