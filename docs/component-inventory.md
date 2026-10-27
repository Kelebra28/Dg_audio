# Catálogo e Inventario de Componentes — DG Audiosound

Este documento contiene el catálogo de componentes clasificados según Atomic Design para el sitio web de **DG Audiosound**, detallando su archivo CSS y módulo JavaScript asociado.

---

## 1. Tokens y Fundamentos (`styles/00-tokens/`)

| Token / Archivo | Ubicación | Descripción |
| :--- | :--- | :--- |
| `variables.css` | `styles/00-tokens/variables.css` | Paleta de colores (oro, negro, blanco, gris), tipografías (Outfit, Inter), sombras y radios de curvatura. |
| `reset.css` | `styles/00-tokens/reset.css` | Reset CSS universal, normalización de box-sizing y estilos base del cuerpo de la página. |

---

## 2. Átomos (`styles/01-atoms/`)

| Átomo | Archivo CSS | Descripción |
| :--- | :--- | :--- |
| **Botones** | `styles/01-atoms/buttons.css` | `.btn`, `.btn-primary`, `.btn-secondary`, `.cookie-button`, efectos hover y glow. |
| **Tipografía** | `styles/01-atoms/typography.css` | Encabezados `h1` a `h6`, textos destacados `.eyebrow`, párrafos y utilidades de alineación. |
| **Badges y Etiquetas** | `styles/01-atoms/badges.css` | Etiquetas de categoría, chips y píldoras decorativas. |
| **Campos de Formulario** | `styles/01-atoms/inputs.css` | Inputs de texto, textareas, estilos de focus y contenedor select. |
| **WhatsApp Flotante** | `styles/01-atoms/floating-whatsapp.css` | Botón flotante inferior `.whatsapp-float` con ícono de Font Awesome. |

---

## 3. Moléculas (`styles/02-molecules/` y `scripts/molecules/`)

| Molécula | Archivo CSS | Archivo JS | Descripción |
| :--- | :--- | :--- | :--- |
| **Enlaces de Navegación** | `styles/02-molecules/nav-items.css` | `scripts/organisms/navbar.js` | Enlaces del navbar con subrayado animado y detección activa. |
| **Tarjeta de Solución** | `styles/02-molecules/service-card.css` | N/A | Bloque visual de solución con imagen de fondo y texto sobrepuesto. |
| **Tarjeta de Aplicación** | `styles/02-molecules/product-card.css` | `scripts/molecules/filter-tabs.js` | Sub-items interactivos con revelado de descripción en hover (`.hover-desc`). |
| **Filtros de Categoría** | `styles/02-molecules/filter-tabs.css` | `scripts/molecules/filter-tabs.js` | Botonera interactiva para alternar visibilidad de productos/aplicaciones. |
| **Barra de Confianza** | `styles/02-molecules/trust-bar.css` | N/A | Estadísticas e indicadores clave con cifras numéricas destacadas. |
| **Banner de Cookies** | `styles/02-molecules/cookie-banner.css` | `scripts/molecules/cookie-consent.js` | Cuadro de diálogo de consentimiento compatible con Google Consent Mode v2. |
| **Selector Personalizado** | `styles/01-atoms/inputs.css` | `scripts/molecules/custom-select.js` | Menú desplegable personalizado para el campo de tipo de proyecto en formulario. |

---

## 4. Organismos (`styles/03-organisms/` y `scripts/organisms/`)

| Organismo | Archivo CSS | Archivo JS | ID / Clase HTML |
| :--- | :--- | :--- | :--- |
| **Navbar Adaptativo** | `styles/03-organisms/navbar.css` | `scripts/organisms/navbar.js` | `#navbar`, `#hamburger`, `#nav-menu` |
| **Hero Principal** | `styles/03-organisms/hero.css` | `scripts/organisms/hero-slider.js` | `.hero`, `#inicio` |
| **Dark Premium** | `styles/03-organisms/dark-premium.css` | N/A | `.section-dark-premium` |
| **Premium White** | `styles/03-organisms/premium-white.css` | N/A | `.section-premium-white` |
| **Soluciones** | `styles/03-organisms/solutions.css` | N/A | `.solutions`, `#soluciones` |
| **Aplicaciones** | `styles/03-organisms/applications.css` | `scripts/molecules/filter-tabs.js` | `.applications`, `#aplicaciones` |
| **Proceso de Trabajo** | `styles/03-organisms/how-we-work.css` | N/A | `.how-we-work`, `#proceso` |
| **Nosotros (Why Us)** | `styles/03-organisms/why-us.css` | N/A | `.why-us`, `#nosotros` |
| **Marcas Aliadas** | `styles/03-organisms/brands.css` | N/A | `.brands`, `#marcas` |
| **Preguntas Frecuentes** | `styles/03-organisms/faq.css` | `scripts/organisms/faq-accordion.js` | `.faq`, `#faq` |
| **Contacto y WhatsApp** | `styles/03-organisms/contact.css` | `scripts/organisms/whatsapp-forms.js` | `.contact-bubbles-section`, `#contacto` |
| **Footer** | `styles/03-organisms/footer.css` | N/A | `.footer` |

---

## 5. Páginas (`styles/04-pages/`)

| Archivo | Propósito |
| :--- | :--- |
| `styles/04-pages/home.css` | Espaciados de contenedores, fondos y ajustes visuales exclusivos de la página de inicio. |
