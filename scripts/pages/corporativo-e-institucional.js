/**
 * DG AUDIOSOUND — PÁGINA: CORPORATIVO E INSTITUCIONAL
 * Controla la interactividad del carrusel de sistemas 3D, blueprint interactivo,
 * acordeón FAQ, tilt 3D y formulario de WhatsApp.
 */

export function initCorporativoInstitucionalPage() {
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

    // 5. COMPONENTE ESTRELLA: CAROUSEL PARALLAX 3D (SHOWCASE)
    const showcaseSlides = document.querySelectorAll('.showcase-slide');
    const showcaseNavButtons = document.querySelectorAll('.showcase-nav-btn');
    const infoPanel = document.querySelector('.showcase-info-panel');

    const systemsData = [
        {
            title: "Salas de <strong>Juntas</strong>",
            desc: "Sistemas de videoconferencia con cámaras, microfonía, audio, pantallas y control definidos según la sala, los participantes y las plataformas de colaboración.",
            specs: [
                "Cámaras PTZ, auto-framing o cámaras fijas según el espacio",
                "Microfonía de techo, mesa o inalámbrica según cobertura",
                "Pantallas, colaboración e interfaces de control según plataforma"
            ],
            link: "/corporativo-e-institucional/salas-de-juntas"
        },
        {
            title: "Auditorios <strong>Corporativos</strong>",
            desc: "Refuerzo sonoro, microfonía, proyección o displays y control para auditorios, capacitación, presentaciones y eventos institucionales.",
            specs: [
                "Altavoces y amplificación seleccionados según cobertura y nivel requerido",
                "Proyección o displays de gran formato según distancia, luz y contenido",
                "Control y operación definidos según el flujo de presentaciones"
            ],
            link: "/corporativo-e-institucional/auditorios-corporativos"
        },
        {
            title: "Gobierno y <strong>Cabildos</strong>",
            desc: "Sistemas de discusión, microfonía, cámaras, grabación, transmisión y votación cuando el alcance de la sala lo requiere.",
            specs: [
                "Unidades de discusión y votación cuando el proyecto lo requiere",
                "Cámaras con encuadre o seguimiento según la dinámica de la sala",
                "Grabación y transmisión integradas según requerimientos"
            ],
            link: "/corporativo-e-institucional/gobierno"
        },
        {
            title: "Oficinas <strong>Corporativas</strong>",
            desc: "Audio distribuido, salas de colaboración, señalización y conectividad audiovisual para áreas de trabajo, recepción y espacios comunes.",
            specs: [
                "Altavoces de plafón o muro seleccionados según cobertura",
                "Amplificación y procesamiento dimensionados según zonas y carga",
                "Cableado, red y racks coordinados con la infraestructura"
            ],
            link: "/corporativo-e-institucional/oficinas-corporativas"
        },
        {
            title: "Educación y <strong>Aulas</strong>",
            desc: "Audio, video y colaboración para aulas híbridas, auditorios académicos e institutos, definidos según modalidad de enseñanza y número de usuarios.",
            specs: [
                "Pantallas interactivas o displays según la dinámica del aula",
                "Cámaras fijas, PTZ o con seguimiento según la clase",
                "Audio de refuerzo o distribución definido según cobertura e inteligibilidad"
            ],
            link: "/corporativo-e-institucional/educacion"
        },
        {
            title: "Hoteles y <strong>Hospitalidad</strong>",
            desc: "Audio ambiental, pantallas y control por zonas para lobbies, pasillos, áreas comunes y espacios de hospitalidad.",
            specs: [
                "Audio ambiental distribuido según cobertura y nivel de ruido",
                "Voceo operativo o integración con sistemas existentes cuando aplica",
                "Control por zonas y programación según el alcance"
            ],
            link: "/corporativo-e-institucional/hoteles"
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

    // 6. LÓGICA DEL BLUEPRINT INTERACTIVO
    const hotspots = document.querySelectorAll('.blueprint-hotspot');
    const bpPanel = document.getElementById('blueprint-details');

    const blueprintData = {
        juntas: {
            header: "Salas de Juntas Inteligentes",
            title: "Colaboración con <strong>audio y video integrados</strong>",
            desc: "Definimos microfonía, cámaras, pantallas, altavoces, procesamiento y conectividad según la geometría de la sala, la posición de los participantes y las plataformas utilizadas.",
            tech1Title: "Microfonía",
            tech1Desc: "Techo, mesa o inalámbrica según diseño",
            tech2Title: "Video",
            tech2Desc: "PTZ, auto-framing o cámara fija según sala"
        },
        auditorio: {
            header: "Ingeniería en Auditorios",
            title: "Refuerzo Acústico <strong>Profesional</strong>",
            desc: "El sistema de un auditorio se define a partir de dimensiones, altura, aforo, ruido, reverberación, cobertura, nivel requerido, contenido y condiciones de visualización.",
            tech1Title: "Dispersión",
            tech1Desc: "Distribuido, arreglos o line array según cálculo",
            tech2Title: "Proyección",
            tech2Desc: "Proyección o displays según distancia y luz"
        },
        recepcion: {
            header: "Audio de Hospitalidad",
            title: "Sonido Ambiental <strong>Homogéneo</strong>",
            desc: "Diseñamos audio distribuido por zonas considerando altura, cobertura, ruido ambiental, separación entre altavoces, uso del espacio y niveles de operación.",
            tech1Title: "Cobertura",
            tech1Desc: "Altavoces seleccionados según patrón de cobertura",
            tech2Title: "Zonificación",
            tech2Desc: "Control Multizona Independiente"
        },
        aulas: {
            header: "Educación Tecnológica",
            title: "Aulas Híbridas <strong>Interactivas</strong>",
            desc: "Integramos audio, cámaras, pantallas y colaboración para modalidades presenciales e híbridas, considerando docentes, alumnos, contenido, plataformas y distribución del aula.",
            tech1Title: "Colaboración",
            tech1Desc: "Pantallas interactivas o displays según uso",
            tech2Title: "Clase Híbrida",
            tech2Desc: "Cámaras fijas, PTZ o con seguimiento según aula"
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

    // 7. ACORDEÓN DE PREGUNTAS (FAQ) CON ROTACIÓN
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
    const cards3D = document.querySelectorAll('.card-lux, .process-bento-item, .gateway-lux-card');
    cards3D.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const percentX = (x / rect.width) * 100;
            const percentY = (y / rect.height) * 100;

            const rotateX = ((rect.height / 2 - y) / (rect.height / 2)) * 8;
            const rotateY = ((x - rect.width / 2) / (rect.width / 2)) * 8;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
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

    // 9. CAPTURA Y FORMULACIÓN DEL WHATSAPP LEAD FORM BURBUJAS
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

            const msg = `🏛️ *DG AUDIOSOUND - SOLICITUD CORPORATIVO E INSTITUCIONAL* 🏛️\n\n` +
                `• *Cliente:* ${name}\n` +
                `• *Empresa:* ${company}\n` +
                `• *Teléfono:* ${phone}\n` +
                `• *Ciudad:* ${city}\n` +
                `• *Tipo de Proyecto:* ${project}\n\n` +
                `📝 *Detalles del Espacio / Proyecto:*\n${message}\n\n` +
                `_Deseo revisar una solución de audio y video para este proyecto._`;

            const urlEncodedMsg = encodeURIComponent(msg);
            const waUrl = `https://wa.me/${tel}?text=${urlEncodedMsg}`;

            window.open(waUrl, '_blank', 'noopener');
        });
    }
}

// Inicialización automática (DOM ready o inmediata si ya está cargado)
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCorporativoInstitucionalPage);
} else {
    initCorporativoInstitucionalPage();
}
