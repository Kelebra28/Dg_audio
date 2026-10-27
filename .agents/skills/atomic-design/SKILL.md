---
name: atomic-design
description: >-
  Operational runbook and architectural standards for refactoring, creating,
  and maintaining UI components, styles, and scripts under Atomic Design methodology
  for the DG Audiosound static project.
---

# Atomic Design Architecture — DG Audiosound

Este documento es la **Skill de referencia técnica y operativa** para trabajar en el proyecto **DG Audiosound**. Establece cómo modularizar, componer y mantener la interfaz gráfica y la lógica funcional mediante la metodología **Atomic Design**, adaptada a una arquitectura estática moderna (Vanilla CSS + ES Modules, sin bundler, 100% compatible con Apache).

---

## 1. Principios Fundamentales

1. **Cero Regresiones Visuales**: Ningún refactor debe modificar selectores, clases, colores, tipografías, breakpoints de media queries ni espaciados de componentes existentes sin aprobación explícita.
2. **Sin Herramientas de Compilación**: No se utiliza npm, webpack ni Vite. El código debe ejecutarse nativamente en el navegador mediante `@import` en CSS y `import`/`export` nativos en JavaScript (`type="module"`).
3. **Compatibilidad con Servidor**: Todos los enlaces y rutas de assets deben ser compatibles con las directivas de `.htaccess` y las políticas de caché de Apache.
4. **Preservación SEO y Tracking**: Los tags de analítica temprana (Consent Mode, GTM, GA4, Meta Pixel), JSON-LD y encabezados semánticos (`<h1>` a `<h6>`) nunca deben verse alterados por la modularización.

---

## 2. Jerarquía de Capas (Atomic Design)

La estructura de carpetas en `styles/` y `scripts/` sigue rigurosamente esta jerarquía de menor a mayor complejidad:

```text
styles/
├── main.css                   # Archivo orquestador maestro (ensambla con @import)
├── 00-tokens/                 # Fundamentos de diseño y resets globales
├── 01-atoms/                  # Elementos indivisibles básicos
├── 02-molecules/              # Combinaciones funcionales de átomos
├── 03-organisms/              # Secciones completas e independientes
└── 04-pages/                  # Estilos y composiciones específicos de página
```

### Capa 0: Tokens y Base (`00-tokens/`)
* **Propósito**: Valores primitivos de diseño y normalización base.
* **Archivos clave**:
  * `variables.css`: Variables CSS nativas (`:root`) con la paleta oficial (dorado `#d4a437`, negro carbón `#0d0d0f`, gris grafito `#1c1f26`), tipografías (`Outfit`, `Inter`), escalas de espaciado (`--space-*`), radios y sombras premium (`--shadow-glow`, etc.).
  * `reset.css`: Reset universal (`* { margin:0; padding:0; box-sizing: border-box; }`) y estilos globales de `html`, `body`.

### Capa 1: Átomos (`01-atoms/`)
* **Propósito**: Elementos HTML unitarios con estilos directos y reutilizables que no pueden dividirse sin perder significado.
* **Archivos clave**:
  * `buttons.css`: Botones de acción (`.btn`, `.btn-primary`, `.btn-secondary`, `.cookie-button`, estados `:hover`, `:focus`).
  * `typography.css`: Jerarquía tipográfica (`h1`-`h6`, `.eyebrow`, subtítulos, lead texts, párrafos estándar).
  * `badges.css`: Etiquetas de estado, chips y badges de categoría.
  * `inputs.css`: Campos de formulario, textareas, labels e indicadores de foco.
  * `floating-whatsapp.css`: Botón flotante de WhatsApp (`.whatsapp-float`) y microanimaciones de pulso.

### Capa 2: Moléculas (`02-molecules/`)
* **Propósito**: Conjuntos simples de 2 o más átomos que funcionan como una unidad visual interactiva.
* **Archivos clave**:
  * `nav-items.css`: Enlaces de navegación con indicador de sección activa (`.nav-link`, `.active`).
  * `service-card.css`: Tarjetas de soluciones o servicios individuales con imagen, título y descripción emergente (`.hover-desc`).
  * `product-card.css`: Tarjetas de aplicaciones o catálogo con soporte para filtros (`.product-card`, `.sub-item`).
  * `cookie-banner.css`: Banner emergente de consentimiento de privacidad (`.cookie-consent`, acciones de aceptar/rechazar).
  * `filter-tabs.css`: Botonera de filtrado interactivo (`.filter-btn`).
  * `trust-bar.css`: Barra de indicadores y credenciales de confianza (`.trust-bar`).

### Capa 3: Organismos (`03-organisms/`)
* **Propósito**: Secciones completas de la interfaz construidas a partir de moléculas y átomos, con identidad temática clara.
* **Archivos clave**:
  * `navbar.css`: Cabecera fija flotante adaptativa con logo, menú, botón de contacto y responsive drawer (`#navbar`, `#hamburger`, `#nav-menu`).
  * `hero.css`: Sección principal con slider de fondos fotográficos, textos y llamados a la acción (`.hero`, `.slide`, `.hero-kicker`).
  * `solutions.css`: Malla o catálogo de soluciones integrales (`.solutions`).
  * `applications.css`: Malla interactiva de aplicaciones segmentada por verticales (`.applications`, `.app-category-block`).
  * `how-we-work.css`: Sección de metodología y proceso paso a paso (`.how-we-work`).
  * `why-us.css`: Bloque institucional con pilares de valor (`.why-us`).
  * `brands.css`: Carrusel o grilla de marcas aliadas y fabricantes oficiales (`.brands`).
  * `faq.css`: Acordeón interactivo de preguntas y respuestas (`.faq`, `.accordion-header`).
  * `contact.css`: Formularios de contacto dinámicos vía WhatsApp (formulario premium y formulario de burbujas).
  * `footer.css`: Pie de página con enlaces institucionales, datos de contacto y avisos legales (`.footer`, `.footer-bottom`).

### Capa 4: Páginas (`04-pages/`)
* **Propósito**: Estilos exclusivos de una vista o plantilla en particular que no se comparten globalmente.
* **Archivos clave**:
  * `home.css`: Ajustes de flujo vertical, paddings de contenedor y composiciones específicas de `index.html`.

---

## 3. Arquitectura de CSS (`styles/main.css`)

El archivo `styles/main.css` es el único punto de entrada enlazado en el HTML. Ensambla las capas en estricto orden de especificidad:

```css
/* ==========================================================================
   DG AUDIOSOUND — MASTER STYLESHEET (ATOMIC DESIGN)
   ========================================================================== */

/* 1. Tokens & Base */
@import './00-tokens/variables.css';
@import './00-tokens/reset.css';

/* 2. Atoms */
@import './01-atoms/typography.css';
@import './01-atoms/buttons.css';
@import './01-atoms/badges.css';
@import './01-atoms/inputs.css';
@import './01-atoms/floating-whatsapp.css';

/* 3. Molecules */
@import './02-molecules/nav-items.css';
@import './02-molecules/service-card.css';
@import './02-molecules/product-card.css';
@import './02-molecules/filter-tabs.css';
@import './02-molecules/trust-bar.css';
@import './02-molecules/cookie-banner.css';

/* 4. Organisms */
@import './03-organisms/navbar.css';
@import './03-organisms/hero.css';
@import './03-organisms/solutions.css';
@import './03-organisms/applications.css';
@import './03-organisms/how-we-work.css';
@import './03-organisms/why-us.css';
@import './03-organisms/brands.css';
@import './03-organisms/faq.css';
@import './03-organisms/contact.css';
@import './03-organisms/footer.css';

/* 5. Pages */
@import './04-pages/home.css';
```

---

## 4. Arquitectura de JavaScript (ES Modules Nativos)

Para evitar la contaminación del objeto global `window` y permitir dependencias claras:

1. **Punto de Entrada**: `<script type="module" src="/scripts/main.js"></script>` al final del `<body>`.
2. **Estructura de Módulos**:
   * Cada módulo en `scripts/molecules/` o `scripts/organisms/` exporta una función inicializadora pura (ejemplo: `export function initNavbar() { ... }`).
   * No se ejecutan efectos secundarios al importar un módulo; la ejecución ocurre explícitamente en el orquestador principal.
3. **Orquestador Principal (`scripts/main.js`)**:
   ```javascript
   import { initNavbar } from './organisms/navbar.js';
   import { initHeroSlider } from './organisms/hero-slider.js';
   import { initScrollReveal } from './organisms/scroll-reveal.js';
   import { initFaqAccordion } from './organisms/faq-accordion.js';
   import { initFilterTabs } from './molecules/filter-tabs.js';
   import { initWhatsAppForms } from './organisms/whatsapp-forms.js';
   import { initCustomSelect } from './molecules/custom-select.js';
   import { initCookieConsent } from './molecules/cookie-consent.js';

   document.addEventListener('DOMContentLoaded', () => {
       initNavbar();
       initHeroSlider();
       initScrollReveal();
       initFaqAccordion();
       initFilterTabs();
       initWhatsAppForms();
       initCustomSelect();
       initCookieConsent();
   });
   ```

---

## 5. Procedimiento Operativo para Refactorizaciones

Cuando se refactorice una página o componente en este repositorio, el agente debe seguir obligatoriamente este checklist:

1. **Copia de Seguridad**: Verificar que el archivo original exista en `_legacy/`.
2. **Extracción Quirúrgica**: Extraer bloques de CSS sin alterar nombres de clase ni reglas de selector.
3. **Aislamiento de Responsabilidad**:
   * Si es un elemento reutilizable sin dependencias de sección -> Átomo o Molécula.
   * Si es una sección estructural completa del layout -> Organismo.
   * Si es un ajuste exclusivo de una sola URL -> Página.
4. **Verificación en Navegador**:
   * Levantar servidor local (`python3 -m http.server 8000`).
   * Navegar y comprobar visualmente con la herramienta de navegador.
   * Revisar consola: Cero errores 404 y cero advertencias de JavaScript.
