document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('main .card-body');

    
    const searchInput = document.getElementById('searchInput');
    const categorySelect = document.getElementById('categorySelectDesktop');
    const filterButton = document.getElementById('filterBtnDesktop'); // تغییر به id اختصاصی

    const searchInputMobile = document.getElementById('searchInputMobile');
    const categorySelectMobile = document.getElementById('categorySelectMobile');
    const filterBtnMobile = document.getElementById('filterBtnMobile');

    function filterPosts(searchText, category) {
        cards.forEach(card => {
            const title = card.querySelector('.card-title').textContent.toLowerCase();
            const description = card.querySelector('.card-text').textContent.toLowerCase();
            const cardCategory = card.getAttribute('data-category').toLowerCase();

            const matchesText = title.includes(searchText) || description.includes(searchText);
            const matchesCategory = category === "" || cardCategory === category;

            if (matchesText && matchesCategory) {
                card.parentElement.style.display = 'block';
            } else {
                card.parentElement.style.display = 'none';
            }
        });
    }

    filterButton.addEventListener("click", () => {
        const searchText = searchInput.value.toLowerCase();
        const category = categorySelect.value.toLowerCase();
        filterPosts(searchText, category);
    });

    
    filterBtnMobile.addEventListener("click", () => {
        const searchText = searchInputMobile.value.toLowerCase();
        const category = categorySelectMobile.value.toLowerCase();
        filterPosts(searchText, category);
    });
});
