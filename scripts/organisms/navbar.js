/**
 * DG AUDIOSOUND — ORGANISMO: NAVBAR FLOTANTE ADAPTATIVO
 * Maneja el cambio de fondo claro/oscuro por IntersectionObserver,
 * la contracción al hacer scroll y el menú hamburguesa móvil.
 */

export function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    // Secciones con fondo claro -> el navbar se vuelve claro con texto oscuro
    const lightSections = document.querySelectorAll(
        '.section-light, .section-light-alt, .section-premium-white, .trust-bar-wrapper, .brands, .solutions, .how-we-work, .contact-bubbles-section'
    );

    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navbar.classList.add('nav-light');
            }
        });
    }, { rootMargin: '-70px 0px 0px 0px', threshold: 0.01 });

    // Secciones con fondo oscuro -> el navbar vuelve a vidrio oscuro
    const darkSections = document.querySelectorAll(
        '.hero, .section-dark, .section-black, .section-dark-premium, .applications, .faq, .why-us'
    );

    const darkNavObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navbar.classList.remove('nav-light');
            }
        });
    }, { rootMargin: '-70px 0px 0px 0px', threshold: 0.01 });

    lightSections.forEach(s => navObserver.observe(s));
    darkSections.forEach(s => darkNavObserver.observe(s));

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Menú móvil (hamburguesa)
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Cerrar menú al hacer clic en un enlace
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                
                navLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            });
        });
    }
}
