/**
 * DG AUDIOSOUND — ORQUESTADOR PRINCIPAL DE JAVASCRIPT (ES MODULES)
 * Importa e inicializa los módulos atómicos de forma limpia y desacoplada.
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
