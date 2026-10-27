/**
 * DG AUDIOSOUND — PÁGINA: NEGOCIOS Y EXPERIENCIAS
 * Controla la interactividad del carrusel comercial 3D, blueprint interactivo,
 * acordeón FAQ, tilt 3D y formularios de cotización de WhatsApp.
 */

export function initNegociosExperienciasPage() {
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

    // 5. COMPONENTE ESTRELLA: CAROUSEL PARALLAX 3D (COMERCIAL)
    const showcaseSlides = document.querySelectorAll('.showcase-slide');
    const showcaseNavButtons = document.querySelectorAll('.showcase-nav-btn');
    const infoPanel = document.querySelector('.showcase-info-panel');

    const systemsData = [
        {
            title: "Audio para <strong>Restaurantes</strong>",
            desc: "Música ambiental distribuida de forma uniforme para áreas interiores, terrazas y zonas de servicio, cuidando el confort acústico del comensal.",
            specs: [
                "Bocinas de plafón o muro premium",
                "Control multizonas para interior y terraza",
                "Integración de pantallas para eventos deportivos"
            ],
            link: "/negocios-y-experiencias/restaurantes"
        },
        {
            title: "Sistemas para <strong>Bares y Antros</strong>",
            desc: "Sistemas de sonido de alto impacto con subwoofers, consolas de mezcla, monitoreo e integración de iluminación cuando el proyecto lo requiera.",
            specs: [
                "Bocinas PA y subwoofers comerciales",
                "Consolas de mezcla y monitoreo para DJ",
                "Iluminación complementaria rítmica"
            ],
            link: "/negocios-y-experiencias/bares-antros"
        },
        {
            title: "Audio para <strong>Gimnasios y Fitness</strong>",
            desc: "Sonido de alta potencia y definición para clases grupales dirigidas, recepción, áreas de pesas y cardio que motiva a tus clientes.",
            specs: [
                "Bocinas comerciales de alta potencia",
                "Micrófonos inalámbricos de diadema para coach",
                "Distribución de zonas con volumen independiente"
            ],
            link: "/negocios-y-experiencias/gimnasios"
        },
        {
            title: "Sonido para <strong>Cafeterías</strong>",
            desc: "Música de fondo cálida y agradable que genera una atmósfera de confort, propicia para trabajar, conversar o relajarse.",
            specs: [
                "Bocinas discretas de alta calidad",
                "Reproductor integrado fácil de operar",
                "Calibración de volumen bajo y presencia nítida"
            ],
            link: "/negocios-y-experiencias/cafeterias"
        },
        {
            title: "Señalización y Audio para <strong>Retail</strong>",
            desc: "Branding sonoro comercial, pantallas de gran formato y video walls para comunicar promociones y crear experiencias en tiendas de ropa y retail.",
            specs: [
                "Bocinas empotrables de alta fidelidad",
                "Video walls y señalización digital dinámica",
                "Sistemas de voceo e intercomunicadores"
            ],
            link: "/negocios-y-experiencias/retail"
        },
        {
            title: "Experiencias en <strong>Barberías</strong>",
            desc: "Atmósfera acústica cuidada con música moderna y pantallas para entretenimiento de tus clientes mientras esperan o reciben servicio.",
            specs: [
                "Bocinas estéticas con gran fidelidad",
                "Instalación de pantallas HD y conectividad",
                "Control centralizado e intuitivo desde tablet"
            ],
            link: "/negocios-y-experiencias/barberias"
        }
    ];

    if (showcaseNavButtons.length && infoPanel) {
        showcaseNavButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const index = parseInt(btn.getAttribute('data-index'), 10);
                if (isNaN(index) || !systemsData[index]) return;

                infoPanel.classList.remove('active');

                setTimeout(() => {
                    showcaseSlides.forEach(slide => slide.classList.remove('active'));
                    showcaseNavButtons.forEach(navBtn => navBtn.classList.remove('active'));

                    if (showcaseSlides[index]) showcaseSlides[index].classList.add('active');
                    btn.classList.add('active');

                    const data = systemsData[index];
                    const titleEl = infoPanel.querySelector('.showcase-slide-title');
                    const descEl = infoPanel.querySelector('.showcase-slide-desc');
                    const linkEl = infoPanel.querySelector('.gateway-lux-link');
                    const specsList = infoPanel.querySelector('.showcase-specs');

                    if (titleEl) titleEl.innerHTML = data.title;
                    if (descEl) descEl.textContent = data.desc;
                    if (linkEl) linkEl.setAttribute('href', data.link);

                    if (specsList) {
                        specsList.innerHTML = '';
                        data.specs.forEach(spec => {
                            const li = document.createElement('li');
                            li.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${spec}`;
                            specsList.appendChild(li);
                        });
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
            header: "Audio por Zonas",
            title: "Distribución <strong>Multizona</strong>",
            desc: "Planificamos el control de volumen por áreas independientes. Permite tener música ambiental a nivel moderado en el salón comedor, mientras que en la terraza o barra el audio tiene mayor protagonismo.",
            tech1Title: "Zonas",
            tech1Desc: "Comedor, terraza, barra, baños",
            tech2Title: "Operación",
            tech2Desc: "Control por app móvil centralizado"
        },
        audio: {
            header: "Música Ambiental",
            title: "Presencia <strong>Nítida y Agradable</strong>",
            desc: "Definimos cantidad, ubicación, orientación y nivel de los altavoces considerando altura, cobertura, ruido ambiental y condiciones acústicas del local.",
            tech1Title: "Bocinas",
            tech1Desc: "Distribución uniforme de alta gama",
            tech2Title: "Fidelidad",
            tech2Desc: "Rango optimizado para voz y música"
        },
        jardin: {
            header: "Sistemas de Video",
            title: "Video Walls <strong>y Pantallas</strong>",
            desc: "Integramos señalización digital y distribución de video para enviar contenido, eventos deportivos o comunicación comercial a múltiples pantallas.",
            tech1Title: "Visual",
            tech1Desc: "Pantallas UHD y videowalls",
            tech2Title: "Distribución",
            tech2Desc: "Distribución AV según distancias y fuentes"
        },
        hifi: {
            header: "Control Comercial",
            title: "Operación <strong>Simplificada</strong>",
            desc: "Organizamos la electrónica en un rack técnico adecuado y simplificamos los controles para que el personal opere las funciones previstas sin acceder a configuraciones innecesarias.",
            tech1Title: "Seguridad",
            tech1Desc: "Limitadores y racks bajo llave",
            tech2Title: "Uso",
            tech2Desc: "Panel táctil o botonera de pared"
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
                    const headerEl = document.getElementById('bp-header');
                    const titleEl = document.getElementById('bp-title');
                    const descEl = document.getElementById('bp-desc');
                    const tech1Title = document.getElementById('bp-tech1-title');
                    const tech1Desc = document.getElementById('bp-tech1-desc');
                    const tech2Title = document.getElementById('bp-tech2-title');
                    const tech2Desc = document.getElementById('bp-tech2-desc');

                    if (headerEl) headerEl.textContent = data.header;
                    if (titleEl) titleEl.innerHTML = data.title;
                    if (descEl) descEl.textContent = data.desc;
                    if (tech1Title) tech1Title.textContent = data.tech1Title;
                    if (tech1Desc) tech1Desc.textContent = data.tech1Desc;
                    if (tech2Title) tech2Title.textContent = data.tech2Title;
                    if (tech2Desc) tech2Desc.textContent = data.tech2Desc;

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
            const name = document.getElementById('cb-name')?.value.trim() || '';
            const company = document.getElementById('cb-company')?.value.trim() || 'No especificada';
            const phone = document.getElementById('cb-phone')?.value.trim() || '';
            const city = document.getElementById('cb-city')?.value.trim() || '';
            const project = document.getElementById('cb-project')?.value || 'Comercial';
            const message = document.getElementById('cb-message')?.value.trim() || '';
            const tel = '525537270177';

            const msg = `🏛️ *DG AUDIOSOUND - SOLICITUD DE ASESORÍA COMERCIAL* 🏛️\n\n` +
                `• *Cliente:* ${name}\n` +
                `• *Empresa:* ${company}\n` +
                `• *Teléfono:* ${phone}\n` +
                `• *Ciudad:* ${city}\n` +
                `• *Tipo de Proyecto:* ${project}\n\n` +
                `📝 *Detalles del Espacio / Proyecto:*\n${message}\n\n` +
                `_Deseo coordinar una asesoría personalizada para mi espacio comercial._`;

            const waUrl = `https://wa.me/${tel}?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');
        });
    }
}

// Auto-inicialización
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNegociosExperienciasPage);
} else {
    initNegociosExperienciasPage();
}
