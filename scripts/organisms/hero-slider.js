/**
 * DG AUDIOSOUND — ORGANISMO: HERO SLIDER
 * Controla la rotación automática de fondos y textos del kicker del hero.
 */

export function initHeroSlider() {
    const slides = document.querySelectorAll('.slide');
    const heroKicker = document.querySelector('.hero-kicker');
    if (!slides.length) return;

    let currentSlide = 0;
    const slideInterval = 5000;

    const kickerTexts = [
        "Residencial Premium",
        "Negocios y Experiencias Comerciales",
        "Corporativo e Institucional",
        "Eventos y Producción"
    ];

    // Carga diferida de imágenes de fondo para slides no iniciales
    setTimeout(() => {
        slides.forEach(slide => {
            const bgClass = slide.getAttribute('data-bg-class');
            if (bgClass) {
                slide.classList.add(bgClass);
                slide.removeAttribute('data-bg-class');
            }
        });
    }, 2500);

    setInterval(() => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
        
        if (heroKicker && kickerTexts[currentSlide]) {
            heroKicker.textContent = kickerTexts[currentSlide];
        }
    }, slideInterval);
}
