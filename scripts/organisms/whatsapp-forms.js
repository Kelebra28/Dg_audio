/**
 * DG AUDIOSOUND — ORGANISMO: FORMULARIOS DE CONTACTO VÍA WHATSAPP
 * Captura datos de formularios (Premium y Burbujas) y abre la URL codificada de WhatsApp.
 */

export function initWhatsAppForms() {
    const tel = "525537270177";

    // 1. Formulario Premium de Asesoría
    const premiumForm = document.getElementById('premiumWhatsappForm');
    if (premiumForm) {
        premiumForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const name = document.getElementById('p-name')?.value || '';
            const company = document.getElementById('p-company')?.value || "No especificada";
            const email = document.getElementById('p-email')?.value || '';
            const phone = document.getElementById('p-phone')?.value || '';
            const city = document.getElementById('p-city')?.value || '';
            const project = document.getElementById('p-project')?.value || '';
            const budget = document.getElementById('p-budget')?.value || "No especificado";
            const message = document.getElementById('p-message')?.value || '';
            
            const text = `Hola DG Audiosound! 👋\n\nHe completado el formulario de asesoría:\n\n*Nombre:* ${name}\n*Empresa:* ${company}\n*Email:* ${email}\n*Teléfono:* ${phone}\n*Ciudad:* ${city}\n*Tipo de Proyecto:* ${project}\n*Presupuesto:* ${budget}\n\n*Detalles del proyecto:*\n${message}`;
            const whatsappUrl = `https://wa.me/${tel}?text=${encodeURIComponent(text)}`;
            window.open(whatsappUrl, '_blank');
        });
    }

    // 2. Formulario de Burbujas de Contacto
    const bubblesForm = document.getElementById('bubblesWhatsappForm');
    if (bubblesForm) {
        bubblesForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name    = document.getElementById('cb-name')?.value || '';
            const company = document.getElementById('cb-company')?.value || 'No especificada';
            const phone   = document.getElementById('cb-phone')?.value || '';
            const city    = document.getElementById('cb-city')?.value || '';
            const project = document.getElementById('cb-project')?.value || '';
            const message = document.getElementById('cb-message')?.value || '';
            
            const text = `Hola DG Audiosound! 👋\n\nSolicito asesoría:\n\n*Nombre:* ${name}\n*Empresa:* ${company}\n*Teléfono:* ${phone}\n*Ciudad:* ${city}\n*Tipo de Proyecto:* ${project}\n\n*Detalles:*\n${message}`;
            window.open(`https://wa.me/${tel}?text=${encodeURIComponent(text)}`, '_blank');
        });
    }
}
