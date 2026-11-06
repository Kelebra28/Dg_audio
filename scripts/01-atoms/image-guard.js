/**
 * ==========================================================================
 * DG AUDIOSOUND — ÁTOMO: IMAGE & ASSET SELF-HEALING GUARD
 * Previene saturación de peticiones concurrentes (HTTP 429) con lazy-loading
 * y recupera automáticamente cualquier imagen o fondo que haya quedado en
 * caché con error 429 en el proxy CDN de Vercel.
 * ==========================================================================
 */

export function initImageGuard() {
    let queueDelay = 0;
    const STEP_MS = 220;

    function buildFallbackUrl(originalUrl) {
        try {
            const parsed = new URL(originalUrl, window.location.href);
            if (!parsed.pathname.includes('/assets/')) return null;

            // 1er intento: usar ?v=3 en el mismo dominio (rompe caché 429 de Vercel)
            if (!parsed.searchParams.has('v')) {
                parsed.searchParams.set('v', '3');
                return parsed.href;
            }
            // 2do intento: cargar directo del origen Hostinger (sin pasar por Vercel)
            if (parsed.hostname === 'www.dgaudiosound.com' || parsed.hostname === 'dgaudiosound.com') {
                return `https://html.dgaudiosound.com${parsed.pathname}`;
            }
        } catch (e) {}
        return null;
    }

    function healImage(img) {
        const attempts = Number(img.dataset.healAttempts || '0');
        if (attempts >= 2) return;
        const currentSrc = img.currentSrc || img.src;
        if (!currentSrc) return;

        const nextUrl = buildFallbackUrl(currentSrc);
        if (!nextUrl) return;

        img.dataset.healAttempts = String(attempts + 1);
        const delay = queueDelay;
        queueDelay += STEP_MS;

        setTimeout(() => {
            if (img.hasAttribute('srcset')) {
                img.removeAttribute('srcset');
            }
            img.src = nextUrl;
        }, delay);
    }

    const allImages = document.querySelectorAll('img');
    allImages.forEach((img, index) => {
        // Activar lazy-loading en imágenes fuera del primer pantallazo
        if (index > 2 && !img.classList.contains('logo-img') && !img.hasAttribute('loading')) {
            img.setAttribute('loading', 'lazy');
        }

        img.addEventListener('error', () => healImage(img));

        // Si ya terminó de cargar con error (naturalWidth === 0) antes de que corriera el script
        if (img.complete && img.naturalWidth === 0) {
            healImage(img);
        }
    });

    // Verificar fondos inline (style="background-image: url(...)")
    const bgElements = document.querySelectorAll('[style*="background-image"]');
    bgElements.forEach((el) => {
        const styleAttr = el.getAttribute('style') || '';
        const match = styleAttr.match(/url\(['"]?([^'")]+)['"]?\)/);
        if (!match || !match[1]) return;

        const rawUrl = match[1];
        const resolvedUrl = new URL(rawUrl, window.location.href).href;
        const probe = new Image();
        probe.onerror = () => {
            const fallback = buildFallbackUrl(resolvedUrl);
            if (!fallback) return;
            const delay = queueDelay;
            queueDelay += STEP_MS;
            setTimeout(() => {
                el.style.backgroundImage = `url('${fallback}')`;
            }, delay);
        };
        probe.src = resolvedUrl;
    });
}

