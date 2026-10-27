/**
 * DG AUDIOSOUND — MOLÉCULA: SELECTOR DESPLEGABLE PERSONALIZADO
 * Maneja el dropdown customizado para el selector de tipo de proyecto en el formulario.
 */

export function initCustomSelect() {
    const customSelect = document.getElementById('customSelectWrapper');
    if (!customSelect) return;

    const trigger = customSelect.querySelector('.premium-select-custom');
    const options = customSelect.querySelectorAll('.premium-option-item');
    const hiddenSelect = document.getElementById('p-project');
    const label = document.getElementById('p-project-label');

    if (!trigger || !hiddenSelect || !label) return;

    trigger.addEventListener('click', (e) => {
        e.stopPropagation();
        customSelect.classList.toggle('active');
    });

    options.forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const val = option.getAttribute('data-value');
            const text = option.textContent;
            
            label.textContent = text;
            hiddenSelect.value = val;
            
            options.forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            
            customSelect.classList.remove('active');
        });
    });

    document.addEventListener('click', () => {
        customSelect.classList.remove('active');
    });
}
