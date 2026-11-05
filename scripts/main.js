/**
 * DG AUDIOSOUND — ORQUESTADOR PRINCIPAL DE JAVASCRIPT (CONSOLIDADO PARA PRODUCCIÓN)
 * Todos los módulos atómicos integrados en un único archivo para evitar HTTP 429 (Too Many Requests)
 * en servidores compartidos / CDN al cargar múltiples ES Modules concurrentes.
 */

/* --------------------------------------------------------------------------
 * 1. ORGANISMO: NAVBAR FLOTANTE ADAPTATIVO
 * -------------------------------------------------------------------------- */
export function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    const lightSections = document.querySelectorAll(
        '.section-light, .section-light-alt, .section-white, .section-premium-white, .trust-bar-wrapper, .brands, .solutions, .how-we-work, .contact-bubbles-section, .section-lux-white, .section-lux-gray'
    );

    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navbar.classList.add('nav-light');
            }
        });
    }, { rootMargin: '-70px 0px 0px 0px', threshold: 0.01 });

    const darkSections = document.querySelectorAll(
        '.hero, .corp-hero-v2, .hero-lux, .section-dark, .section-black, .section-dark-premium, .applications, .faq, .why-us, .section-lux-dark, .section-lux-dark-alt, .lux-dark-section'
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
    }, { passive: true });

    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

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

/* --------------------------------------------------------------------------
 * 2. ORGANISMO: HERO SLIDER
 * -------------------------------------------------------------------------- */
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

    setTimeout(() => {
        slides.forEach(slide => {
            const bgClass = slide.getAttribute('data-bg-class');
            if (bgClass) {
                slide.classList.add(bgClass);
                slide.removeAttribute('data-bg-class');
            }
        });
    }, 2500);

    if (slides.length > 1) {
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');

            if (heroKicker && kickerTexts[currentSlide] && document.querySelector('.hero')) {
                heroKicker.textContent = kickerTexts[currentSlide];
            }
        }, slideInterval);
    }
}

/* --------------------------------------------------------------------------
 * 3. ORGANISMO: SCROLL REVEAL Y NAVEGACIÓN SUAVE
 * -------------------------------------------------------------------------- */
export function initScrollReveal() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const id = this.getAttribute('href');
            if (id === "#") return;

            const target = document.querySelector(id);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -20px 0px',
        threshold: 0.05
    };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                entry.target.classList.add('revealed');
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal, .reveal-lux');
    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            el.classList.add('active');
            el.classList.add('revealed');
        }
        revealObserver.observe(el);
    });
}

/* --------------------------------------------------------------------------
 * 4. ORGANISMO: ACORDEÓN DE PREGUNTAS FRECUENTES (FAQ)
 * -------------------------------------------------------------------------- */
export function initFaqAccordion() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const activeHeader = document.querySelector('.accordion-header.active');
            if (activeHeader && activeHeader !== header) {
                activeHeader.classList.remove('active');
                if (activeHeader.nextElementSibling) {
                    activeHeader.nextElementSibling.style.maxHeight = null;
                }
            }

            header.classList.toggle('active');
            const content = header.nextElementSibling;
            if (!content) return;

            if (header.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = null;
            }
        });
    });
}

/* --------------------------------------------------------------------------
 * 5. ORGANISMO: FORMULARIOS DE CONTACTO VÍA WHATSAPP
 * -------------------------------------------------------------------------- */
export function initWhatsAppForms() {
    const tel = "525537270177";

    const premiumForm = document.getElementById('premiumWhatsappForm');
    if (premiumForm) {
        premiumForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('p-name')?.value || '';
            const company = document.getElementById('p-company')?.value || "No especificada";
            const email = document.getElementById('p-email')?.value || '';
            const phone = document.getElementById('p-phone')?.value || '';
            const city = document.getElementById('p-city')?.value || '';
            const project = document.getElementById('p-project')?.value || '';
            const budget = document.getElementById('p-budget')?.value || "No especificado";
            const message = document.getElementById('p-message')?.value || '';

            const text = `Hola DG Audiosound! 👋\n\nHe completado el formulario de asesoría:\n\n*Nombre:* ${name}\n*Empresa:* ${company}\n*Email:* ${email}\n*Teléfono:* ${phone}\n*Ciudad:* ${city}\n*Tipo de Proyecto:* ${project}\n*Presupuesto:* ${budget}\n\n*Detalles del proyecto:*\n${message}`;
            const whatsappUrl = `https://wa.me/${tel}?text=${encodeURIComponent(text)}`;
            window.open(whatsappUrl, '_blank');
        });
    }

    const bubblesForm = document.getElementById('bubblesWhatsappForm');
    if (bubblesForm) {
        bubblesForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name    = document.getElementById('cb-name')?.value || '';
            const company = document.getElementById('cb-company')?.value || 'No especificada';
            const phone   = document.getElementById('cb-phone')?.value || '';
            const city    = document.getElementById('cb-city')?.value || '';
            const project = document.getElementById('cb-project')?.value || '';
            const message = document.getElementById('cb-message')?.value || '';

            const text = `Hola DG Audiosound! 👋\n\nSolicito asesoría:\n\n*Nombre:* ${name}\n*Empresa:* ${company}\n*Teléfono:* ${phone}\n*Ciudad:* ${city}\n*Tipo de Proyecto:* ${project}\n\n*Detalles:*\n${message}`;
            window.open(`https://wa.me/${tel}?text=${encodeURIComponent(text)}`, '_blank');
        });
    }
}

/* --------------------------------------------------------------------------
 * 6. MOLÉCULA: PESTAÑAS DE FILTRADO INTERACTIVO
 * -------------------------------------------------------------------------- */
export function initFilterTabs() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const products = document.querySelectorAll('.product-card');
    if (!filterBtns.length) return;

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            products.forEach(product => {
                product.style.display = 'none';
                product.classList.remove('active');

                if (filterValue === 'all' || product.classList.contains(filterValue)) {
                    product.style.display = 'flex';
                    setTimeout(() => {
                        product.classList.add('active');
                    }, 50);
                }
            });
        });
    });
}

/* --------------------------------------------------------------------------
 * 7. MOLÉCULA: SELECTOR DESPLEGABLE PERSONALIZADO
 * -------------------------------------------------------------------------- */
export function initCustomSelect() {
    const customSelect = document.getElementById('customSelectWrapper');
    if (!customSelect) return;

    const trigger = customSelect.querySelector('.premium-select-custom');
    const options = customSelect.querySelectorAll('.premium-option-item');
    const hiddenSelect = document.getElementById('p-project');
    const label = document.getElementById('p-project-label');

    if (!trigger || !hiddenSelect || !label) return;

    trigger.addEventListener('click', (e) => {
        e.stopPropagation();
        customSelect.classList.toggle('active');
    });

    options.forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const val = option.getAttribute('data-value');
            const text = option.textContent;

            label.textContent = text;
            hiddenSelect.value = val;

            options.forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');

            customSelect.classList.remove('active');
        });
    });

    document.addEventListener('click', () => {
        customSelect.classList.remove('active');
    });
}

/* --------------------------------------------------------------------------
 * 8. MOLÉCULA: BANNER DE CONSENTIMIENTO Y COOKIES
 * -------------------------------------------------------------------------- */
export function initCookieConsent() {
    const cookieBanner = document.getElementById('cookieConsentBanner');
    const acceptCookiesButton = document.getElementById('acceptCookies');
    const rejectCookiesButton = document.getElementById('rejectCookies');
    const openCookiePreferences = document.getElementById('openCookiePreferences');

    function getStoredCookieConsent() {
        try {
            return window.localStorage.getItem('dg_cookie_consent');
        } catch (error) {
            return null;
        }
    }

    function setStoredCookieConsent(value) {
        try {
            window.localStorage.setItem('dg_cookie_consent', value);
        } catch (error) {
            // localStorage bloqueado o no disponible
        }
    }

    function updateDGConsent(consentValue, source) {
        const accepted = consentValue === 'accepted';
        if (typeof window.dgConsentCommand === 'function' && typeof window.dgBuildConsentState === 'function') {
            window.dgConsentCommand(
                'consent',
                'update',
                window.dgBuildConsentState(accepted ? 'granted' : 'denied')
            );
        }

        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            event: accepted ? 'cookie_consent_accepted' : 'cookie_consent_rejected',
            consent_status: consentValue,
            consent_source: source || 'cookie_banner'
        });
    }

    function showCookieBanner() {
        if (!cookieBanner) return;
        cookieBanner.hidden = false;
        cookieBanner.classList.add('is-visible');
    }

    function hideCookieBanner() {
        if (!cookieBanner) return;
        cookieBanner.classList.remove('is-visible');
        cookieBanner.hidden = true;
    }

    function handleCookieChoice(choice) {
        setStoredCookieConsent(choice);
        updateDGConsent(choice, 'cookie_banner');
        hideCookieBanner();
    }

    const storedCookieConsent = getStoredCookieConsent();
    if (!storedCookieConsent) {
        showCookieBanner();
    }

    if (acceptCookiesButton) {
        acceptCookiesButton.addEventListener('click', () => handleCookieChoice('accepted'));
    }

    if (rejectCookiesButton) {
        rejectCookiesButton.addEventListener('click', () => handleCookieChoice('rejected'));
    }

    if (openCookiePreferences) {
        openCookiePreferences.addEventListener('click', () => {
            showCookieBanner();
            if (acceptCookiesButton) acceptCookiesButton.focus();
        });
    }
}

/* --------------------------------------------------------------------------
 * INICIALIZACIÓN PRINCIPAL
 * -------------------------------------------------------------------------- */
function startApp() {
    if (window.__DG_APP_INITIALIZED__) return;
    window.__DG_APP_INITIALIZED__ = true;

    initNavbar();
    initHeroSlider();
    initScrollReveal();
    initFaqAccordion();
    initFilterTabs();
    initWhatsAppForms();
    initCustomSelect();
    initCookieConsent();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startApp);
} else {
    startApp();
}
