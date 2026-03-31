// ── Mobile header toggle ──
const hamburger = document.getElementById('hamburger');
const navMenu   = document.getElementById('nav-menu');

function isMobile() { return window.innerWidth <= 900; }

// Mostrar/ocultar hamburger según viewport
function syncHamburger() {
  hamburger.style.display = isMobile() ? 'block' : 'none';
  if (!isMobile()) navMenu.classList.remove('open');
}

syncHamburger();
window.addEventListener('resize', syncHamburger);

hamburger.addEventListener('click', () => {
  navMenu.classList.toggle('open');
  hamburger.innerHTML = navMenu.classList.contains('open')
    ? '<i class="bi bi-x-lg"></i>'
    : '<i class="bi bi-list"></i>';
});

// ── Mobile: abrir dropdowns con click ──
document.querySelectorAll('[data-toggle="dropdown"]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!isMobile()) return;
    e.stopPropagation();
    btn.nextElementSibling.classList.toggle('open');
  });
});

document.querySelectorAll('[data-toggle="submenu"]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!isMobile()) return;
    e.stopPropagation();
    btn.nextElementSibling.classList.toggle('open');
  });
});

// ── Cerrar al click fuera ──
document.addEventListener('click', e => {
  if (!e.target.closest('.site-nav')) {
    document.querySelectorAll('.dropdown-menu-custom.open, .submenu.open')
      .forEach(el => el.classList.remove('open'));
  }
});
