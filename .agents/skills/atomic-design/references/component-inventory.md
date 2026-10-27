# Inventario de Componentes — DG Audiosound

Este inventario documenta el mapeo de cada elemento de la página principal (`index.html`) a su correspondiente categoría de Atomic Design, su archivo de estilos CSS y su módulo JavaScript asociado.

---

## 1. Tokens y Base (`styles/00-tokens/`)

| Archivo | Elementos / Selectores Mapeados | Descripción |
| :--- | :--- | :--- |
| `variables.css` | `:root { --color-*, --space-*, --shadow-*, --font-* }` | Definición de tokens globales corporativos y diseño premium. |
| `reset.css` | `*, *::before, *::after, html, body` | Resets de márgenes, box-sizing, smooth-scroll base y fondo global. |

---

## 2. Átomos (`styles/01-atoms/`)

| Archivo | Clases / Selectores Principales | Archivo JS Relacionado |
| :--- | :--- | :--- |
| `typography.css` | `h1, h2, h3, h4, .eyebrow, .section-title, .lead-p` | N/A |
| `buttons.css` | `.btn, .btn-primary, .btn-secondary, .btn-glow, .cookie-button` | N/A |
| `badges.css` | `.badge, .tag, .status-indicator` | N/A |
| `inputs.css` | `.form-group, input, textarea, .custom-select` | N/A |
| `floating-whatsapp.css` | `.whatsapp-float, .whatsapp-float:hover` | N/A |

---

## 3. Moléculas (`styles/02-molecules/` y `scripts/molecules/`)

| Componente | Archivo CSS | Archivo JS | Descripción |
| :--- | :--- | :--- | :--- |
| **Nav Items** | `nav-items.css` | N/A (gestionado en `navbar.js`) | Enlaces del menú, estados hover y línea indicadora. |
| **Service Card** | `service-card.css` | N/A | Tarjetas de soluciones con animación hover y revelado. |
| **Product Card / Sub-items** | `product-card.css` | `filter-tabs.js` | Tarjetas de aplicaciones (`.sub-item`, `.hover-desc`). |
| **Filter Tabs** | `filter-tabs.css` | `filter-tabs.js` | Botonera interactiva para alternar categorías (`.filter-btn`). |
| **Trust Bar** | `trust-bar.css` | N/A | Barra de métricas y cifras clave (`.trust-item`). |
| **Cookie Banner** | `cookie-banner.css` | `cookie-consent.js` | Banner emergente de consentimiento y Consent Mode GTM. |
| **Custom Select** | `inputs.css` | `custom-select.js` | Dropdown interactivo personalizado de selección de proyectos. |

---

## 4. Organismos (`styles/03-organisms/` y `scripts/organisms/`)

| Organismo | Sección / ID HTML | Archivo CSS | Archivo JS |
| :--- | :--- | :--- | :--- |
| **Navbar** | `<header id="navbar">` | `navbar.css` | `navbar.js` |
| **Hero Slider** | `<section class="hero" id="inicio">` | `hero.css` | `hero-slider.js` |
| **Dark Premium Section** | `<section class="section-dark-premium">` | `dark-premium.css` | N/A |
| **Premium White Section** | `<section class="section-premium-white">` | `premium-white.css` | N/A |
| **Solutions Grid** | `<section class="solutions" id="soluciones">` | `solutions.css` | N/A |
| **Applications Grid** | `<section class="applications" id="aplicaciones">` | `applications.css` | `filter-tabs.js` |
| **How We Work (Proceso)** | `<section class="how-we-work" id="proceso">` | `how-we-work.css` | N/A |
| **Why Us (Nosotros)** | `<section class="why-us" id="nosotros">` | `why-us.css` | N/A |
| **Brands Grid** | `<section class="brands" id="marcas">` | `brands.css` | N/A |
| **FAQ Accordion** | `<section class="faq" id="faq">` | `faq.css` | `faq-accordion.js` |
| **Contact Bubbles Form** | `<section class="contact-bubbles-section" id="contacto">` | `contact.css` | `whatsapp-forms.js` |
| **Footer** | `<footer class="footer">` | `footer.css` | N/A |

---

## 5. Páginas (`styles/04-pages/`)

| Archivo | Propósito |
| :--- | :--- |
| `home.css` | Estilos exclusivos y espaciados generales aplicables únicamente a `index.html`. |
