# Arquitectura Atomic Design — DG Audiosound

Este documento detalla la arquitectura técnica de interfaz de usuario de **DG Audiosound**, implementada bajo la metodología **Atomic Design** en una pila estática nativa (Vanilla CSS + ES Modules, sin dependencias de Node.js ni herramientas de compilación).

---

## 1. Motivación y Objetivos

El código original mantenía más de 5,200 líneas de estilos incrustadas directamente dentro de `index.html` en una etiqueta `<style>`, dificultando el mantenimiento, reutilización y lectura del código. 

Con esta arquitectura:
1. **Separación de Responsabilidades**: El archivo HTML vuelve a ser un documento estructural semántico limpio.
2. **Escalabilidad y Modularidad**: Cada botón, tarjeta o sección vive en su propio archivo atómico.
3. **Mantenimiento sin Fricción**: Modificar el diseño de la barra de navegación o los acordeones de FAQ requiere editar únicamente su componente respectivo.
4. **Cero Dependencias**: Se ejecuta directamente en cualquier servidor Apache sin necesidad de compilar con `npm build`.

---

## 2. Los Cinco Niveles de Atomic Design

```
+--------------------------------------------------------------+
| 04-PAGES        (home.css, layouts específicos)              |
+--------------------------------------------------------------+
| 03-ORGANISMS    (navbar, hero, soluciones, faq, footer)      |
+--------------------------------------------------------------+
| 02-MOLECULES    (service-card, nav-items, cookie-banner)     |
+--------------------------------------------------------------+
| 01-ATOMS        (buttons, badges, inputs, floating-whatsapp) |
+--------------------------------------------------------------+
| 00-TOKENS       (variables.css, reset.css)                   |
+--------------------------------------------------------------+
```

### 2.1. Tokens (`styles/00-tokens/`)
Almacena las variables CSS nativas que configuran la identidad visual de la marca:
* **Colores**: Oro corporativo (`--color-primary: #d4a437`), negro carbón (`--color-bg-dark-alt: #0d0d0f`), blanco base y grises plata.
* **Tipografías**: `Outfit` para títulos y encabezados; `Inter` para cuerpos de texto.
* **Espaciados y Sombras**: Escalas estandarizadas de márgenes y radios de borde.

### 2.2. Átomos (`styles/01-atoms/`)
Componentes unitarios que no pueden descomponerse más:
* Botones (`.btn`, `.btn-primary`, `.btn-secondary`, `.cookie-button`).
* Títulos y párrafos globales (`h1`-`h6`, `.eyebrow`).
* Inputs de formulario y botón flotante de WhatsApp.

### 2.3. Moléculas (`styles/02-molecules/` y `scripts/molecules/`)
Combinaciones de átomos con propósito funcional específico:
* Tarjetas de servicio y de aplicaciones con revelado hover (`.sub-item`, `.hover-desc`).
* Banner de consentimiento de cookies y gestión del Consent Mode.
* Pestañas de filtrado interactivo para el catálogo de soluciones.

### 2.4. Organismos (`styles/03-organisms/` y `scripts/organisms/`)
Secciones completas del sitio:
* **Navbar**: Barra de navegación fija con detector de fondo claro/oscuro por `IntersectionObserver` y menú hamburguesa móvil.
* **Hero Slider**: Carrusel con rotación automática de fondos y textos dinámicos.
* **Soluciones & Aplicaciones**: Bloques de servicios estructurados.
* **FAQ**: Acordeón interactivo accesible.
* **Contacto**: Formularios vinculados a WhatsApp API.
* **Footer**: Pie de página institucional y legal.

### 2.5. Páginas (`styles/04-pages/`)
Composiciones y espaciados particulares para una vista específica, como `home.css`.

---

## 3. Integración en el HTML

En el documento principal `index.html`:

```html
<!-- Hoja de Estilos Maestra (ensamblada vía @import) -->
<link rel="stylesheet" href="/styles/main.css" />

<!-- Módulo Principal de JavaScript (ES Modules nativos) -->
<script type="module" src="/scripts/main.js"></script>
```

---

## 4. Gobernanza y Mantenimiento

* **Skill de IA**: El asistente Antigravity cuenta con la Skill `.agents/skills/atomic-design/SKILL.md` que le permite operar y refactorizar componentes respetando estas reglas.
* **Convenciones**: Consultar `.agents/skills/atomic-design/references/conventions.md` para reglas de nomenclatura y especificidad.
