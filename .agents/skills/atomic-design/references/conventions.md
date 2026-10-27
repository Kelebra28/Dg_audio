# Convenciones de Código — Atomic Design DG Audiosound

Este documento describe los estándares de codificación, nomenclatura y buenas prácticas que rigen la arquitectura Atomic Design del proyecto.

---

## 1. Convenciones de CSS

### 1.1. Nomenclatura de Archivos y Selectores
* **Archivos**: En minúsculas y separados por guiones (`kebab-case`).
  * Ejemplos: `service-card.css`, `cookie-banner.css`, `floating-whatsapp.css`.
* **Clases**: Usar nomenclatura descriptiva y semántica. Si se utiliza estructura tipo BEM o derivada:
  * Bloque: `.service-card`
  * Elemento: `.service-card-title`, `.service-card-img`
  * Modificador: `.btn-primary`, `.btn-secondary`, `.is-active`
* **Evitar Selectores Genéricos No Calificados**: Evitar reglas directas a etiquetas como `div { ... }` o `p { ... }` fuera de `reset.css` o `typography.css`. Todos los estilos de componentes deben estar encapsulados por clases.

### 1.2. Variables CSS (Tokens de Diseño)
Todos los valores de color, espaciado y tipografía deben consumir los tokens definidos en `variables.css`:
* **Colores**:
  * `--color-bg`, `--color-bg-alt`, `--color-bg-dark`, `--color-bg-dark-alt`, `--color-black`
  * `--color-primary` (`#d4a437`), `--color-primary-hover` (`#a97b17`)
  * `--color-text-dark`, `--color-text-muted`, `--color-text-light`, `--color-text-white`
  * `--color-silver` (`#c9ccd3`), `--color-accent`
* **Tipografías**:
  * `--font-heading`: `'Outfit', sans-serif`
  * `--font-body`: `'Inter', sans-serif`
* **Espaciados**:
  * `--space-sm` (0.5rem), `--space-md` (1rem), `--space-lg` (2rem), `--space-xl` (4rem), `--space-xxl` (6rem)
* **Sombras y Efectos**:
  * `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-glow`
* **Radios y Transiciones**:
  * `--radius-sm` (8px), `--radius-md` (12px), `--radius-lg` (20px)
  * `--transition-fast` (0.2s), `--transition-base` (0.3s), `--transition-slow` (0.5s)

### 1.3. Breakpoints de Media Queries
Usar exclusivamente los breakpoints canónicos del proyecto:
* Móvil: `max-width: 768px`
* Tablet: `min-width: 769px and max-width: 1024px`
* Escritorio: `min-width: 1025px`
* Pantallas grandes: `min-width: 1400px`

---

## 2. Convenciones de JavaScript (ES Modules)

### 2.1. Módulos Puros
* Cada archivo de script debe exportar una función de inicialización con nombre (`export function init[NombreComponente]()`).
* Ningún módulo debe ejecutar código al momento de ser importado; la inicialización se delega a `main.js` tras el evento `DOMContentLoaded`.
* Verificar siempre la existencia de los elementos del DOM antes de adjuntar `addEventListener`:
  ```javascript
  export function initHeroSlider() {
      const slides = document.querySelectorAll('.slide');
      if (!slides.length) return; // Salida temprana si no está en la página actual
      // ...
  }
  ```

### 2.2. Aislamiento de Variables
* Prohibido declarar variables en el ámbito global `window` a menos que sea un requisito expreso de analítica externa (como `window.DG_TRACKING_CONFIG` o `window.dataLayer`).
* Utilizar `const` y `let` con alcance de bloque.

---

## 3. Preservación y Cero Regresiones

* Al extraer estilos del bloque monolítico de `index.html`, no se deben alterar valores numéricos de `padding`, `margin`, `font-size` ni colores hexadecimales.
* Todo componente refactorizado debe verificarse en el navegador con la consola de desarrollador abierta para confirmar 0 errores.
