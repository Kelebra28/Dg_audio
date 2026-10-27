/**
 * DG AUDIOSOUND — SUBPAGE MODULE (ATOMIC DESIGN)
 * Motor interactivo compartido para todas las subpáginas de solución
 * (Residencial, Negocios, Corporativo, Eventos)
 */

export function initSubpage(options = {}) {
    if (window.__DG_SUBPAGE_INITIALIZED__) return;
    window.__DG_SUBPAGE_INITIALIZED__ = true;

    // --- 1. ADAPTIVE FLOATING NAVBAR COLOR ---
    const navbarEl = document.getElementById('navbar');
    if (navbarEl) {
        const checkNavbarColor = () => {
            const navbarRect = navbarEl.getBoundingClientRect();
            const navbarCenter = navbarRect.top + navbarRect.height / 2;

            const sections = document.querySelectorAll('section, header');
            let currentSection = null;

            sections.forEach(sec => {
                if (sec.id === 'navbar') return;
                const rect = sec.getBoundingClientRect();
                if (rect.top <= navbarCenter && rect.bottom >= navbarCenter) {
                    currentSection = sec;
                }
            });

            if (currentSection) {
                const isLight = currentSection.classList.contains('section-light') ||
                    currentSection.classList.contains('section-light-alt') ||
                    currentSection.classList.contains('section-white') ||
                    currentSection.classList.contains('contact-bubbles-section') ||
                    currentSection.classList.contains('breadcrumb-wrap');
                if (isLight) {
                    navbarEl.classList.remove('nav-light');
                } else {
                    navbarEl.classList.add('nav-light');
                }
            }
        };

        window.addEventListener('scroll', checkNavbarColor, { passive: true });
        window.addEventListener('resize', checkNavbarColor, { passive: true });

        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbarEl.classList.add('scrolled');
            } else {
                navbarEl.classList.remove('scrolled');
            }
        }, { passive: true });

        checkNavbarColor();
    }

    // --- 2. EFECTO INTERACTIVO DE INCLINACIÓN Y REFLEJO ESPEJO 3D ---
    const cards3D = document.querySelectorAll('.benefit-v2-card, .process-bento-item, .include-card, .brand-marquee-item, .antithesis-problem-card');
    cards3D.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const percentX = (x / rect.width) * 100;
            const percentY = (y / rect.height) * 100;

            const rotateX = ((rect.height / 2 - y) / (rect.height / 2)) * 10;
            const rotateY = ((x - rect.width / 2) / (rect.width / 2)) * 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.03, 1.03, 1.03)`;
            card.style.setProperty('--mouse-x', `${percentX}%`);
            card.style.setProperty('--mouse-y', `${percentY}%`);

            card.style.setProperty('--glow-x', `${(percentX - 50) * 2}%`);
            card.style.setProperty('--glow-y', `${(percentY - 50) * 2}%`);
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            card.style.setProperty('--mouse-x', '50%');
            card.style.setProperty('--mouse-y', '50%');
            card.style.setProperty('--glow-x', '0%');
            card.style.setProperty('--glow-y', '0%');
        });
    });

    // --- 3. ACORDEÓN DE PREGUNTAS (FAQ) CON ROTACIÓN ---
    const faqItems = document.querySelectorAll('.faq-lux-item');
    faqItems.forEach(item => {
        const btn = item.querySelector('.faq-lux-btn');
        const answer = item.querySelector('.faq-lux-answer');
        if (!btn || !answer) return;

        btn.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            faqItems.forEach(i => {
                i.classList.remove('active');
                const a = i.querySelector('.faq-lux-answer');
                if (a) a.style.maxHeight = '0px';
            });

            if (!isActive) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });

    // --- 4. MANEJADOR DEL HERO SLIDER (SLIDESHOW CROSSFADE) ---
    const slides = document.querySelectorAll('.corp-hero-v2 .slide');
    let currentSlide = 0;
    const slideInterval = 4000;

    if (slides.length > 0) {
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, slideInterval);
    }

    // --- 5. MANEJADOR DEL FORMULARIO DE COTIZACIÓN DE DOBLE BURBUJA ---
    const bubblesForm = document.getElementById('bubblesWhatsappForm');
    if (bubblesForm) {
        bubblesForm.addEventListener('submit', function (event) {
            event.preventDefault();
            if (!bubblesForm.reportValidity()) return;

            const name = document.getElementById('cb-name')?.value.trim() || '';
            const projectName = document.getElementById('cb-company')?.value.trim() || 'No especificado';
            const phone = document.getElementById('cb-phone')?.value.trim() || '';
            const city = document.getElementById('cb-city')?.value.trim() || '';
            const projectType = document.getElementById('cb-project')?.value || options.defaultProjectType || 'Cine en Casa';
            const details = document.getElementById('cb-message')?.value.trim() || '';

            const pageHeading = options.pageTitle || document.querySelector('.corp-hero-v2 h1')?.innerText.replace(/\s+/g, ' ').trim() || 'SOLUCIÓN RESIDENCIAL';

            const msg =
                `🎬 *DG Audiosound - ${pageHeading.toUpperCase()}* 🎬\n\n` +
                `• *Cliente:* ${name}\n` +
                `• *Residencia / Proyecto:* ${projectName}\n` +
                `• *Teléfono:* ${phone}\n` +
                `• *Ciudad:* ${city}\n` +
                `• *Tipo de Proyecto:* ${projectType}\n\n` +
                `📝 *Detalles del Proyecto:*\n${details}\n\n` +
                `_Deseo recibir asesoría para evaluar este proyecto audiovisual._`;

            const waUrl = `https://wa.me/525537270177?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank', 'noopener');
        });
    }
}

// Auto-inicialización si el DOM ya está listo o en DOMContentLoaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => initSubpage());
} else {
    initSubpage();
}
