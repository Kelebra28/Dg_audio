/**
 * DG AUDIOSOUND — ORQUESTADOR PRINCIPAL DE JAVASCRIPT (ATOMIC DESIGN)
 * Inicializa todos los módulos de organismos y moléculas de la interfaz.
 * NOTA: Al editar cualquier módulo atómico, ejecuta `npm run build` para
 * actualizar `scripts/bundle.min.js` (usado en producción para evitar HTTP 429).
 */

import { initNavbar } from './organisms/navbar.js';
import { initHeroSlider } from './organisms/hero-slider.js';
import { initScrollReveal } from './organisms/scroll-reveal.js';
import { initFaqAccordion } from './organisms/faq-accordion.js';
import { initWhatsAppForms } from './organisms/whatsapp-forms.js';
import { initFilterTabs } from './molecules/filter-tabs.js';
import { initCustomSelect } from './molecules/custom-select.js';
import { initCookieConsent } from './molecules/cookie-consent.js';

function startApp() {
    if (window.__DG_APP_INITIALIZED__) return;
    window.__DG_APP_INITIALIZED__ = true;

    initNavbar();
    initHeroSlider();
    initScrollReveal();
    initFaqAccordion();
    initFilterTabs();
    initWhatsAppForms();
    initCustomSelect();
    initCookieConsent();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startApp);
} else {
    startApp();
}
