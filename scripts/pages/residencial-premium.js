/**
 * DG AUDIOSOUND — PÁGINA: RESIDENCIAL PREMIUM
 * Controla interactividad del carrusel de sistemas, blueprint acústico,
 * acordeón FAQ, tilt 3D y formularios de consulta.
 */

export function initResidencialPremiumPage() {
    // 1. HERO SLIDESHOW CROSSFADE LENTO
    const heroSlides = document.querySelectorAll('.hero-lux-slide');
    if (heroSlides.length > 1) {
        let currentHeroIndex = 0;
        setInterval(() => {
            heroSlides[currentHeroIndex].classList.remove('active');
            currentHeroIndex = (currentHeroIndex + 1) % heroSlides.length;
            heroSlides[currentHeroIndex].classList.add('active');
        }, 5500);
    }

    // 2. MOTOR REVEAL CON INTERSECTION OBSERVER DE ALTO RENDIMIENTO
    const revealElements = document.querySelectorAll('.reveal-lux');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.05,
        rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            el.classList.add('revealed');
        }
        revealObserver.observe(el);
    });

    // 3. SCROLL-DRIVEN PARALLAX ASIMÉTRICO
    let lastScrollTop = 0;
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        if (scrollTop === lastScrollTop) return;
        lastScrollTop = scrollTop;

        document.documentElement.style.setProperty('--scroll-offset', scrollTop);

        // Proceso: Activar etapas según scroll
        const processSection = document.getElementById('proceso');
        if (processSection) {
            const rect = processSection.getBoundingClientRect();
            const processItems = document.querySelectorAll('.process-lux-item');

            if (rect.top < window.innerHeight * 0.6) {
                const progress = Math.min(Math.max((window.innerHeight * 0.6 - rect.top) / rect.height, 0), 1);
                const step = Math.floor(progress * 4);
                processItems.forEach((item, index) => {
                    if (index <= step) {
                        item.classList.add('active');
                    } else {
                        item.classList.remove('active');
                    }
                });
            }
        }
    }, { passive: true });

    // 4. ADAPTIVE FLOATING NAVBAR COLOR
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
                const isLight = currentSection.classList.contains('section-lux-white') ||
                    currentSection.classList.contains('section-lux-gray') ||
                    currentSection.classList.contains('contact-bubbles-section');
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

    // 5. CAROUSEL PARALLAX 3D (SHOWCASE)
    const showcaseSlides = document.querySelectorAll('.showcase-slide');
    const showcaseNavButtons = document.querySelectorAll('.showcase-nav-btn');
    const infoPanel = document.querySelector('.showcase-info-panel');

    const systemsData = [
        {
            title: "Cine en <strong>Casa</strong>",
            desc: "Diseñamos e integramos sistemas de cine en casa para salas dedicadas y espacios de entretenimiento, considerando tamaño de imagen, distancia de visualización, audio envolvente, subwoofers, amplificación, cableado y calibración.",
            specs: [
                "Pantallas o proyección 4K HDR según el espacio",
                "Audio envolvente y Dolby Atmos cuando aplique",
                "Instalación, configuración y calibración profesional"
            ],
            link: "/residencial-premium/cine-en-casa"
        },
        {
            title: "Audio <strong>Distribuido</strong>",
            desc: "Música en distintas áreas de la casa con bocinas de plafón, muro o soluciones discretas, amplificación multizona y control sencillo desde dispositivos compatibles.",
            specs: [
                "Audio por zonas para salas, recámaras y áreas sociales",
                "Bocinas y amplificación dimensionadas según cada espacio",
                "Control de volumen y fuentes según la solución"
            ],
            link: "/residencial-premium/audio-distribuido"
        },
        {
            title: "Audio <strong>Hi-Fi</strong>",
            desc: "Sistemas estéreo de alta fidelidad diseñados como una cadena completa: fuentes, tornamesa o streamer, amplificación, bocinas, subwoofer, cableado y ubicación según el espacio.",
            specs: [
                "Bocinas de piso o repisa seleccionadas para la sala",
                "Amplificación y fuentes compatibles con el sistema",
                "Tornamesas, streamers y DACs según tus hábitos de escucha"
            ],
            link: "/residencial-premium/audio-hi-fi"
        },
        {
            title: "Family <strong>Room</strong>",
            desc: "Audio y video para salas familiares donde películas, deportes, streaming y videojuegos conviven con una operación sencilla, cableado ordenado e integración estética.",
            specs: [
                "Pantalla dimensionada según distancia y forma de uso",
                "Barra de sonido o audio envolvente según el proyecto",
                "Conectividad para streaming, consolas y otras fuentes"
            ],
            link: "/residencial-premium/family-room"
        },
        {
            title: "Terrazas y <strong>Jardín</strong>",
            desc: "Audio y video para terrazas, jardines, roof gardens y áreas sociales exteriores, considerando cobertura, exposición ambiental, nivel de uso, cableado y control por zonas.",
            specs: [
                "Bocinas adecuadas para exterior según la exposición",
                "Distribución de audio para una cobertura equilibrada",
                "Pantallas o video exterior cuando las condiciones lo permitan"
            ],
            link: "/residencial-premium/terrazas-y-jardin"
        },
        {
            title: "Home <strong>Office</strong>",
            desc: "Soluciones de audio, video, iluminación y conectividad para videoconferencias y trabajo desde casa, diseñadas para mejorar claridad de voz, imagen, orden y facilidad de uso.",
            specs: [
                "Pantallas y soportes dimensionados según el espacio",
                "Microfonía adecuada para mejorar la claridad de voz",
                "Iluminación y conectividad integradas según el espacio"
            ],
            link: "/residencial-premium/home-office"
        }
    ];

    if (showcaseNavButtons.length && infoPanel) {
        showcaseNavButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const index = parseInt(btn.getAttribute('data-index'), 10);
                infoPanel.classList.remove('active');

                setTimeout(() => {
                    showcaseSlides.forEach(slide => slide.classList.remove('active'));
                    showcaseNavButtons.forEach(navBtn => navBtn.classList.remove('active'));

                    if (showcaseSlides[index]) showcaseSlides[index].classList.add('active');
                    btn.classList.add('active');

                    const data = systemsData[index];
                    if (data) {
                        const titleEl = infoPanel.querySelector('.showcase-slide-title');
                        const descEl = infoPanel.querySelector('.showcase-slide-desc');
                        const linkEl = infoPanel.querySelector('.gateway-lux-link');
                        if (titleEl) titleEl.innerHTML = data.title;
                        if (descEl) descEl.textContent = data.desc;
                        if (linkEl) linkEl.setAttribute('href', data.link);

                        const specsList = infoPanel.querySelector('.showcase-specs');
                        if (specsList) {
                            specsList.innerHTML = '';
                            data.specs.forEach(spec => {
                                const li = document.createElement('li');
                                li.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${spec}`;
                                specsList.appendChild(li);
                            });
                        }
                    }

                    infoPanel.classList.add('active');
                }, 500);
            });
        });
    }

    // 6. LÓGICA DEL BLUEPRINT INTERACTIVO
    const hotspots = document.querySelectorAll('.blueprint-hotspot');
    const bpPanel = document.getElementById('blueprint-details');

    const blueprintData = {
        cine: {
            header: "Ingeniería en Cine en Casa",
            title: "Cine en <strong>Casa Dedicado</strong>",
            desc: "Diseñamos la ubicación de bocinas, subwoofers y puntos de escucha considerando las dimensiones del espacio, la cobertura, la distribución del sistema y las condiciones acústicas del proyecto.",
            tech1Title: "Ingeniería",
            tech1Desc: "Configuración envolvente según el proyecto",
            tech2Title: "Calibración",
            tech2Desc: "Calibración y ajuste digital del sistema"
        },
        audio: {
            header: "Ingeniería en Audio Distribuido",
            title: "Audio <strong>Distribuido Multizona</strong>",
            desc: "Diseñamos sistemas de audio distribuido por zonas considerando el tipo de espacio, la cobertura, la ubicación de bocinas, la amplificación y la forma de control para lograr una reproducción uniforme y fácil de operar.",
            tech1Title: "Instalación",
            tech1Desc: "Bocinas de plafón, muro o soluciones discretas",
            tech2Title: "Potencia",
            tech2Desc: "Amplificación multizona dimensionada según el sistema"
        },
        jardin: {
            header: "Ingeniería Exterior",
            title: "Terrazas y <strong>Jardín</strong>",
            desc: "Diseñamos audio para terrazas y jardines considerando cobertura, ubicación de bocinas, exposición ambiental, nivel de uso, cableado y control por zonas para lograr una reproducción equilibrada en exteriores.",
            tech1Title: "Protección",
            tech1Desc: "Equipos seleccionados según la exposición ambiental",
            tech2Title: "Diseño",
            tech2Desc: "Cobertura y ubicación de bocinas según el espacio"
        },
        hifi: {
            header: "Ingeniería Audiófila",
            title: "Escucha <strong>Estéreo Hi-Fi</strong>",
            desc: "Diseñamos sistemas estéreo Hi-Fi considerando la posición de escucha, ubicación de bocinas, características del espacio, amplificación, fuentes y configuración para aprovechar mejor el desempeño del sistema.",
            tech1Title: "Componentes",
            tech1Desc: "Bocinas y amplificación seleccionadas según el sistema",
            tech2Title: "Fidelidad",
            tech2Desc: "Configuración y ajuste según el espacio y los componentes"
        }
    };

    if (hotspots.length && bpPanel) {
        hotspots.forEach(spot => {
            spot.addEventListener('click', (e) => {
                const targetKey = e.currentTarget.getAttribute('data-target');
                const data = blueprintData[targetKey];
                if (!data) return;

                bpPanel.style.opacity = '0';
                bpPanel.style.transform = 'translateY(20px)';

                setTimeout(() => {
                    const h = document.getElementById('bp-header');
                    const t = document.getElementById('bp-title');
                    const d = document.getElementById('bp-desc');
                    const t1t = document.getElementById('bp-tech1-title');
                    const t1d = document.getElementById('bp-tech1-desc');
                    const t2t = document.getElementById('bp-tech2-title');
                    const t2d = document.getElementById('bp-tech2-desc');

                    if (h) h.textContent = data.header;
                    if (t) t.innerHTML = data.title;
                    if (d) d.textContent = data.desc;
                    if (t1t) t1t.textContent = data.tech1Title;
                    if (t1d) t1d.textContent = data.tech1Desc;
                    if (t2t) t2t.textContent = data.tech2Title;
                    if (t2d) t2d.textContent = data.tech2Desc;

                    bpPanel.style.opacity = '1';
                    bpPanel.style.transform = 'none';
                }, 350);
            });
        });
    }

    // 7. ACORDEÓN DE PREGUNTAS (FAQ)
    const faqItems = document.querySelectorAll('.faq-lux-item');
    faqItems.forEach(item => {
        const btn = item.querySelector('.faq-lux-btn');
        const answer = item.querySelector('.faq-lux-answer');

        if (btn && answer) {
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
        }
    });

    // 8. EFECTO INTERACTIVO DE INCLINACIÓN Y REFLEJO ESPEJO 3D
    const cards3D = document.querySelectorAll('.card-lux, .process-bento-item');
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

    // 9. WHATSAPP LEAD FORM BURBUJAS
    const bubblesForm = document.getElementById('bubblesWhatsappForm');
    if (bubblesForm) {
        bubblesForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('cb-name')?.value || '';
            const company = document.getElementById('cb-company')?.value || 'No especificada';
            const phone = document.getElementById('cb-phone')?.value || '';
            const city = document.getElementById('cb-city')?.value || '';
            const project = document.getElementById('cb-project')?.value || '';
            const message = document.getElementById('cb-message')?.value || '';
            const tel = '525537270177';

            const msg = `🏛️ *DG AUDIOSOUND - SOLICITUD DE ASESORÍA RESIDENCIAL* 🏛️\n\n` +
                `• *Cliente:* ${name}\n` +
                `• *Residencia / Proyecto:* ${company}\n` +
                `• *Teléfono:* ${phone}\n` +
                `• *Ciudad:* ${city}\n` +
                `• *Tipo de Proyecto:* ${project}\n\n` +
                `📝 *Detalles del Espacio / Proyecto:*\n${message}\n\n` +
                `_Deseo recibir asesoría para evaluar una solución de audio y video para mi residencia._`;

            const waUrl = `https://wa.me/${tel}?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');
        });
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initResidencialPremiumPage);
} else {
    initResidencialPremiumPage();
}
