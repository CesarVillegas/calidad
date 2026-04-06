document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter');

  counters.forEach(counter => {
    let rawValue = counter.dataset.target.replace(',', '.'); // soporta 84,5
    const target = parseFloat(rawValue);

    // Si no es número → mostrar directo
    if (isNaN(target)) {
      counter.textContent = counter.dataset.target;
      return;
    }

    // Detectar cantidad de decimales
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
});