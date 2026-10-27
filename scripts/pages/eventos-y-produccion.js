/**
 * DG AUDIOSOUND — PÁGINA: EVENTOS Y PRODUCCIÓN
 * Controla la interactividad del carrusel de sistemas 3D, blueprint interactivo,
 * acordeón FAQ, tilt 3D y formulario de WhatsApp.
 */

export function initEventosProduccionPage() {
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
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            el.classList.add('revealed');
        }
        revealObserver.observe(el);
    });

    // 3. SCROLL-DRIVEN PARALLAX ASIMÉTRICO (CPU OPTIMIZADO)
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

    // 3.5. ADAPTIVE FLOATING NAVBAR COLOR
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
                    currentSection.classList.contains('contact-bubbles-section') ||
                    currentSection.classList.contains('section-light') ||
                    currentSection.classList.contains('section-white');
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

    // 4. COMPONENTE ESTRELLA: CAROUSEL PARALLAX 3D
    const showcaseSlides = document.querySelectorAll('.showcase-slide');
    const showcaseNavButtons = document.querySelectorAll('.showcase-nav-btn');
    const infoPanel = document.querySelector('.showcase-info-panel');

    const systemsData = [
        {
            title: "Podcast y <strong>Grabación</strong>",
            desc: "Micrófonos, interfaces, mezcla, monitoreo, grabación y video seleccionados según participantes, formato de contenido, espacio y flujo de trabajo.",
            specs: [
                "Micrófonos e interfaces según número de fuentes",
                "Monitoreo, soportes y distribución de señal",
                "Grabación y video según el flujo de producción"
            ],
            link: "/eventos-y-produccion/podcast"
        },
        {
            title: "Audio y Video para <strong>Streamers</strong>",
            desc: "Audio, cámaras, captura, monitoreo, iluminación funcional y control definidos según plataforma, espacio y formato de transmisión.",
            specs: [
                "Microfonía y monitoreo según la dinámica del creador",
                "Cámaras y captura según resolución y plataforma",
                "Iluminación funcional y organización del flujo de señal"
            ],
            link: "/eventos-y-produccion/streamers"
        },
        {
            title: "Sonidos y <strong>DJ</strong>",
            desc: "PA, subwoofers, mezcla, procesamiento, microfonía y monitoreo dimensionados según audiencia, cobertura, SPL objetivo y tipo de presentación.",
            specs: [
                "Altavoces y subwoofers según cobertura y nivel requerido",
                "Mezcla, procesamiento, protección y número de canales",
                "Microfonía, monitoreo y cableado según el montaje"
            ],
            link: "/eventos-y-produccion/sonidos-dj"
        },
        {
            title: "Centros de <strong>Culto</strong>",
            desc: "Refuerzo sonoro, microfonía, monitoreo, video y transmisión definidos según arquitectura, audiencia y operación del espacio.",
            specs: [
                "Microfonía según número de participantes y movilidad",
                "Cobertura e inteligibilidad para el área de audiencia",
                "Video y transmisión según las necesidades de la congregación"
            ],
            link: "/eventos-y-produccion/centros-de-culto"
        },
        {
            title: "Cine <strong>Independiente</strong>",
            desc: "Proyección o pantallas, audio, reproducción y conectividad para exhibiciones, contenido especial y presentaciones audiovisuales.",
            specs: [
                "Visualización según tamaño, distancia y formato de contenido",
                "Audio y cobertura según sala y posiciones de audiencia",
                "Fuentes, reproducción y distribución de señal"
            ],
            link: "/eventos-y-produccion/cine-independiente"
        },
        {
            title: "Músicos y <strong>Vocalistas</strong>",
            desc: "Microfonía, interfaces, monitoreo, mezcla y grabación para ensayo, contenido, presentación y producción musical.",
            specs: [
                "Micrófonos según voz, instrumento y patrón de captación",
                "Monitoreo personal según número de intérpretes",
                "Interfaces y mezcla según entradas, salidas y grabación"
            ],
            link: "/eventos-y-produccion/musicos-vocalistas"
        }
    ];

    if (showcaseNavButtons.length > 0 && infoPanel) {
        showcaseNavButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const index = parseInt(btn.getAttribute('data-index'));
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

    // 5. LÓGICA DEL BLUEPRINT INTERACTIVO
    const hotspots = document.querySelectorAll('.blueprint-hotspot');
    const bpPanel = document.getElementById('blueprint-details');

    const blueprintData = {
        cine: {
            header: "Audio y Captura",
            title: "Producción de <strong>Audio</strong>",
            desc: "Definimos tipo y cantidad de micrófonos, interfaces, consolas, niveles de señal y monitoreo según las fuentes y el flujo de producción.",
            tech1Title: "Entradas",
            tech1Desc: "Entradas según micrófonos e instrumentos",
            tech2Title: "Operación",
            tech2Desc: "Mezcla y monitoreo según usuarios"
        },
        audio: {
            header: "Sistemas de Microfonía",
            title: "Microfonía <strong>Inalámbrica y RF</strong>",
            desc: "Seleccionamos sistemas y coordinamos frecuencias según cantidad de canales, movilidad, entorno de radiofrecuencia y condiciones del recinto.",
            tech1Title: "Radiofrecuencia",
            tech1Desc: "Coordinación según canales y entorno RF",
            tech2Title: "Formatos",
            tech2Desc: "Mano, diadema, solapa u otros según uso"
        },
        jardin: {
            header: "Refuerzo Sonoro",
            title: "PA <strong>para Eventos y DJ</strong>",
            desc: "Dimensionamos altavoces, subwoofers, amplificación y procesamiento según audiencia, cobertura, SPL objetivo, montaje y contenido.",
            tech1Title: "Dimensionamiento",
            tech1Desc: "Cobertura, carga, potencia y margen operativo",
            tech2Title: "Procesamiento",
            tech2Desc: "DSP, protección y distribución de señal"
        },
        hifi: {
            header: "Producción de Video",
            title: "Video y <strong>Streaming</strong>",
            desc: "Definimos cámaras, captura, mezcla de video, distribución y resolución según plataforma, fuentes, pantallas y flujo de transmisión.",
            tech1Title: "Video",
            tech1Desc: "Resolución y captura según plataforma",
            tech2Title: "Flujo",
            tech2Desc: "Fuentes, mezcla y distribución de señal"
        }
    };

    if (hotspots.length > 0 && bpPanel) {
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

    // 6. ACORDEÓN DE PREGUNTAS (FAQ) CON ROTACIÓN
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

    // 7. EFECTO INTERACTIVO DE INCLINACIÓN Y REFLEJO ESPEJO 3D
    const cards3D = document.querySelectorAll('.card-lux, .process-bento-item, .benefit-v2-card, .include-card');
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

    // 8. CAPTURA Y FORMULACIÓN DEL WHATSAPP LEAD FORM BURBUJAS
    const bubblesForm = document.getElementById('bubblesWhatsappForm');
    if (bubblesForm) {
        bubblesForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('cb-name')?.value?.trim() || '';
            const company = document.getElementById('cb-company')?.value?.trim() || 'No especificada';
            const phone = document.getElementById('cb-phone')?.value?.trim() || '';
            const city = document.getElementById('cb-city')?.value?.trim() || '';
            const project = document.getElementById('cb-project')?.value || '';
            const message = document.getElementById('cb-message')?.value?.trim() || '';
            const tel = '525537270177';

            const msg = `⚡ *DG AUDIOSOUND - SOLICITUD EVENTOS Y PRODUCCIÓN* ⚡\n\n` +
                `• *Cliente:* ${name}\n` +
                `• *Empresa / Creador:* ${company}\n` +
                `• *Teléfono:* ${phone}\n` +
                `• *Ciudad:* ${city}\n` +
                `• *Tipo de Proyecto:* ${project}\n\n` +
                `📝 *Detalles del Proyecto / Setup:*\n${message}\n\n` +
                `_Deseo revisar el alcance técnico y la cotización de mi proyecto._`;

            const urlEncodedMsg = encodeURIComponent(msg);
            const waUrl = `https://wa.me/${tel}?text=${urlEncodedMsg}`;

            window.open(waUrl, '_blank', 'noopener');
        });
    }
}

// Inicialización automática
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initEventosProduccionPage);
} else {
    initEventosProduccionPage();
}
