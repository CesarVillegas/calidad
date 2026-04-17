document.addEventListener('DOMContentLoaded', () => {

  // =========================
  // 🔢 CONTADORES
  // =========================
  const counters = document.querySelectorAll('.counter');

  counters.forEach(counter => {
    let rawValue = counter.dataset.target.replace(',', '.');
    const target = parseFloat(rawValue);

    if (isNaN(target)) {
      counter.textContent = counter.dataset.target;
      return;
    }

    const decimals = (rawValue.split('.')[1] || '').length;

    const duration = 1500;
    const steps = duration / 16;
    const increment = target / steps;

    let current = 0;

    const timer = setInterval(() => {
      current += increment;

      if (current >= target) {
        current = target;
        clearInterval(timer);
      }

      counter.textContent = current.toLocaleString('es-CL', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
      });

    }, 16);
  });


  // =========================
  // CARRUSEL
  // =========================
  const track = document.getElementById("track");

  if (!track) return; // seguridad

  const speed = 3000;
  let autoSlide;

  function moveNext() {
    const first = track.children[0];
    const move = getTranslateValue();

    track.style.transition = "transform 0.6s ease";
    track.style.transform = `translateX(${move})`;

    setTimeout(() => {
      track.style.transition = "none";
      track.style.transform = "translateX(0)";
      track.appendChild(first);
    }, 600);
  }

  function movePrev() {
    const last = track.children[track.children.length - 1];
    const move = getTranslateValue();

    track.style.transition = "none";
    track.insertBefore(last, track.firstChild);
    track.style.transform = move;

    setTimeout(() => {
      track.style.transition = "transform 0.6s ease";
      track.style.transform = "translateX(0)";
    }, 10);
  }
  
  function startAuto() {
    autoSlide = setInterval(moveNext, speed);
  }

  function resetAuto() {
    clearInterval(autoSlide);
    startAuto();
  }

  // ▶ iniciar autoplay
  startAuto();

  // =========================
  // FLECHAS
  // =========================
  const nextBtn = document.getElementById("next");
  const prevBtn = document.getElementById("prev");

  if (nextBtn && prevBtn) {
    nextBtn.addEventListener("click", () => {
      resetAuto();
      moveNext();
    });

    prevBtn.addEventListener("click", () => {
      resetAuto();
      movePrev();
    });
  }

  // =========================
  // PAUSA EN HOVER
  // =========================
  track.addEventListener("mouseenter", () => clearInterval(autoSlide));
  track.addEventListener("mouseleave", startAuto);

});

function getTranslateValue() {
  if (window.innerWidth <= 768) {
    return "-50%"; // 2 visibles
  }
  return "-20%"; // 5 visibles
}
