/**
 * DG AUDIOSOUND — MOLÉCULA: PESTAÑAS DE FILTRADO INTERACTIVO
 * Alterna la visibilidad de tarjetas de productos o catálogo según el atributo data-filter.
 */

export function initFilterTabs() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const products = document.querySelectorAll('.product-card');
    if (!filterBtns.length) return;

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            products.forEach(product => {
                product.style.display = 'none';
                product.classList.remove('active');

                if (filterValue === 'all' || product.classList.contains(filterValue)) {
                    product.style.display = 'flex';
                    setTimeout(() => {
                        product.classList.add('active');
                    }, 50);
                }
            });
        });
    });
}
