/**
 * DG AUDIOSOUND — MOLÉCULA: BANNER DE CONSENTIMIENTO Y COOKIES
 * Gestiona el almacenamiento del consentimiento, actualización del Consent Mode (GTM / GA4 / Pixel)
 * y visualización del diálogo de preferencias.
 */

export function initCookieConsent() {
    const cookieBanner = document.getElementById('cookieConsentBanner');
    const acceptCookiesButton = document.getElementById('acceptCookies');
    const rejectCookiesButton = document.getElementById('rejectCookies');
    const openCookiePreferences = document.getElementById('openCookiePreferences');

    function getStoredCookieConsent() {
        try {
            return window.localStorage.getItem('dg_cookie_consent');
        } catch (error) {
            return null;
        }
    }

    function setStoredCookieConsent(value) {
        try {
            window.localStorage.setItem('dg_cookie_consent', value);
        } catch (error) {
            // localStorage bloqueado o no disponible
        }
    }

    function updateDGConsent(consentValue, source) {
        const accepted = consentValue === 'accepted';
        if (typeof window.dgConsentCommand === 'function' && typeof window.dgBuildConsentState === 'function') {
            window.dgConsentCommand(
                'consent',
                'update',
                window.dgBuildConsentState(accepted ? 'granted' : 'denied')
            );
        }

        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            event: accepted ? 'cookie_consent_accepted' : 'cookie_consent_rejected',
            consent_status: consentValue,
            consent_source: source || 'cookie_banner'
        });
    }

    function showCookieBanner() {
        if (!cookieBanner) return;
        cookieBanner.hidden = false;
        cookieBanner.classList.add('is-visible');
    }

    function hideCookieBanner() {
        if (!cookieBanner) return;
        cookieBanner.classList.remove('is-visible');
        cookieBanner.hidden = true;
    }

    function handleCookieChoice(choice) {
        setStoredCookieConsent(choice);
        updateDGConsent(choice, 'cookie_banner');
        hideCookieBanner();
    }

    const storedCookieConsent = getStoredCookieConsent();
    if (!storedCookieConsent) {
        showCookieBanner();
    }

    if (acceptCookiesButton) {
        acceptCookiesButton.addEventListener('click', () => handleCookieChoice('accepted'));
    }

    if (rejectCookiesButton) {
        rejectCookiesButton.addEventListener('click', () => handleCookieChoice('rejected'));
    }

    if (openCookiePreferences) {
        openCookiePreferences.addEventListener('click', () => {
            showCookieBanner();
            if (acceptCookiesButton) acceptCookiesButton.focus();
        });
    }
}
