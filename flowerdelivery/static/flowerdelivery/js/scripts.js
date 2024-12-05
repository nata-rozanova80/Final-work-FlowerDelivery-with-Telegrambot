document.addEventListener('DOMContentLoaded', () => {
    const cartButtons = document.querySelectorAll('.add-to-cart');

    cartButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.getAttribute('data-id');
            alert(`Товар с ID ${productId} добавлен в корзину!`);
            // Логика для добавления в корзину (AJAX запрос)
        });
    });
});
