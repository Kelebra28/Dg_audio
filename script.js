document.addEventListener('DOMContentLoaded', () => {

    /* ========================================
       1. NAVBAR STICKY & SCROLL EFECTO
       ======================================== */
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    /* ========================================
       2. MENÚ MÓVIL (HAMBURGUESA)
       ======================================== */
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Cerrar menú al hacer clic en un enlace
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            
            // Actualizar clase activa suavemente
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });

    /* ========================================
       3. SMOOTH SCROLL (Opcional, en CSS ya está, pero por precaución)
       ======================================== */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const id = this.getAttribute('href');
            if(id === "#") return;
            
            const target = document.querySelector(id);
            if(target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    /* ========================================
       4. ANIMACIONES DE REVELADO (SCROLL)
       ======================================== */
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Opcional: observer.unobserve(entry.target); para que anime solo una vez
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => revealObserver.observe(el));

    // Forzar activación de elementos visibles al cargar
    setTimeout(() => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                el.classList.add('active');
            }
        });
    }, 100);

    /* ========================================
       5. ACORDEÓN (FAQ)
       ======================================== */
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            // Cerrar otros acordeones si se quiere (modo único abierto)
            const activeHeader = document.querySelector('.accordion-header.active');
            if (activeHeader && activeHeader !== header) {
                activeHeader.classList.remove('active');
                activeHeader.nextElementSibling.style.maxHeight = null;
            }

            // Alternar actual
            header.classList.toggle('active');
            const content = header.nextElementSibling;
            
            if (header.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = null;
            }
        });
    });

    /* ========================================
       6. SIMULADOR DE FILTROS EN TIENDA
       ======================================== */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const products = document.querySelectorAll('.product-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remover active de todos los btns
            filterBtns.forEach(b => b.classList.remove('active'));
            // Añadir al seleccionado
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            products.forEach(product => {
                // Hacer reset de estilos para la animación
                product.style.display = 'none';
                product.classList.remove('active'); // Remover reveal activo

                if (filterValue === 'all' || product.classList.contains(filterValue)) {
                    // Timeout para permitir que el display block tome valor antes de la clase active
                    product.style.display = 'flex';
                    setTimeout(() => {
                        product.classList.add('active'); // Forzar frame animation
                    }, 50);
                }
            });
        });
    });

    /* ========================================
       7. HERO SLIDER LOGIC
       ======================================== */
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
    const slideInterval = 5000; // 5 segundos

    if (slides.length > 0) {
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, slideInterval);
    }

    /* ========================================
       8. FORMULARIO A WHATSAPP
       ======================================== */
    /* ========================================
       8. FORMULARIO A WHATSAPP (PREMIUM)
       ======================================== */
    const premiumForm = document.getElementById('premiumWhatsappForm');
    if (premiumForm) {
        premiumForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Obtener valores
            const name = document.getElementById('p-name').value;
            const company = document.getElementById('p-company').value || "No especificada";
            const email = document.getElementById('p-email').value;
            const phone = document.getElementById('p-phone').value;
            const city = document.getElementById('p-city').value;
            const project = document.getElementById('p-project').value;
            const budget = document.getElementById('p-budget').value || "No especificado";
            const message = document.getElementById('p-message').value;
            
            // Número de WhatsApp (sin el +)
            const tel = "525537270177";
            
            // Construir mensaje
            const text = `Hola DG Audiosound! 👋\n\nHe completado el formulario de asesoría:\n\n*Nombre:* ${name}\n*Empresa:* ${company}\n*Email:* ${email}\n*Teléfono:* ${phone}\n*Ciudad:* ${city}\n*Tipo de Proyecto:* ${project}\n*Presupuesto:* ${budget}\n\n*Detalles del proyecto:*\n${message}`;
            
            // Codificar para URL
            const encodedText = encodeURIComponent(text);
            
            // URL final
            const whatsappUrl = `https://wa.me/${tel}?text=${encodedText}`;
            
            // Abrir en nueva pestaña
            window.open(whatsappUrl, '_blank');
        });
    }

});

/* ========================================
   SUBPAGE CINE EN CASA - VIDEO PREVIEW
   ======================================== */
   document.addEventListener('DOMContentLoaded', () => {
    const cineVideoBtn = document.querySelector('.cine-video-preview button');

    if (cineVideoBtn) {
        cineVideoBtn.addEventListener('click', () => {
            const whatsappUrl = 'https://wa.me/525537270177?text=Hola%20DG%20Audiosound%2C%20quiero%20ver%20ejemplos%20o%20cotizar%20un%20cine%20en%20casa';
            window.open(whatsappUrl, '_blank');
        });
    }

    // ========================================
    // INTERACTIVE MOCKUP: VOLUME SLIDERS
    // ========================================
    const sliders = document.querySelectorAll('.volume-slider');
    
    sliders.forEach(slider => {
        slider.addEventListener('click', (e) => {
            const rect = slider.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const width = rect.width;
            let percent = Math.round((x / width) * 100);
            
            // Constrain
            percent = Math.max(0, Math.min(100, percent));
            
            // Update visual
            const progress = slider.querySelector('.volume-progress');
            const label = slider.parentElement.querySelector('.volume-header span:last-child');
            
            if (progress) progress.style.width = percent + '%';
            if (label) label.textContent = percent + '%';
        });
    });

    // ========================================
    // CUSTOM PREMIUM SELECT LOGIC
    // ========================================
    const customSelect = document.getElementById('customSelectWrapper');
    if (customSelect) {
        const trigger = customSelect.querySelector('.premium-select-custom');
        const options = customSelect.querySelectorAll('.premium-option-item');
        const hiddenSelect = document.getElementById('p-project');
        const label = document.getElementById('p-project-label');

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            customSelect.classList.toggle('active');
        });

        options.forEach(option => {
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                const val = option.getAttribute('data-value');
                const text = option.textContent;
                
                // Update label and hidden select
                label.textContent = text;
                hiddenSelect.value = val;
                
                // Mark as selected
                options.forEach(opt => opt.classList.remove('selected'));
                option.classList.add('selected');
                
                // Close
                customSelect.classList.remove('active');
            });
        });

        // Close when clicking outside
        document.addEventListener('click', () => {
            customSelect.classList.remove('active');
        });
    }
});
