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
    const whatsappForm = document.getElementById('whatsappForm');
    if (whatsappForm) {
        whatsappForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Obtener valores
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const project = document.getElementById('project').value;
            const message = document.getElementById('message').value;
            
            // Número de WhatsApp (sin el +)
            const tel = "525537270177";
            
            // Construir mensaje
            const text = `Hola DG Audiosound! 👋\n\nQuiero cotizar un proyecto:\n\n*Nombre:* ${name}\n*Email:* ${email}\n*Teléfono:* ${phone}\n*Proyecto:* ${project}\n*Mensaje:* ${message}`;
            
            // Codificar para URL
            const encodedText = encodeURIComponent(text);
            
            // URL final
            const whatsappUrl = `https://wa.me/${tel}?text=${encodedText}`;
            
            // Abrir en nueva pestaña
            window.open(whatsappUrl, '_blank');
        });
    }

});
