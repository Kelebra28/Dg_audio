/**
 * DG AUDIOSOUND — ORGANISMO: ACORDEÓN DE PREGUNTAS FRECUENTES (FAQ)
 * Maneja el comportamiento interactivo de apertura y cierre de acordeones con cálculo de scrollHeight.
 */

export function initFaqAccordion() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    if (!accordionHeaders.length) return;

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            // Modo único abierto: cerrar otros acordeones si hay uno activo
            const activeHeader = document.querySelector('.accordion-header.active');
            if (activeHeader && activeHeader !== header) {
                activeHeader.classList.remove('active');
                if (activeHeader.nextElementSibling) {
                    activeHeader.nextElementSibling.style.maxHeight = null;
                }
            }

            // Alternar estado del elemento actual
            header.classList.toggle('active');
            const content = header.nextElementSibling;
            if (!content) return;
            
            if (header.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + "px";
            } else {
                content.style.maxHeight = null;
            }
        });
    });
}
