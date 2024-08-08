document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const searchResultsContainer = document.getElementById('search-results');
    const dropdownList = document.getElementById('dropdown-list');
    const cardBody = document.getElementById('pagination');

    // Search Bar
    if (searchBtn && searchInput && searchResultsContainer) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const searchTerm = searchInput.value.trim();
            if (searchTerm) {
                fetch(`/search?q=${searchTerm}`)
                    .then(response => {
                        if (response.ok) {
                            return response.json();
                        } else {
                            throw new Error('Error fetching search results');
                        }
                    })
                    .then(posts => {
                        searchResultsContainer.innerHTML = '';
                        posts.forEach(post => {
                            const postHTML = `
                                <h2>${post.title}</h2>
                                <p>${post.content}</p>
                            `;
                            searchResultsContainer.innerHTML += postHTML;
                        });
                    })
                    .catch(error => {
                        console.error(error);
                        window.location.href = '/404.html';
                    });
            }
        });
    }

    // Add dropdown list items
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    if (dropdownItems.length > 0) {
        dropdownItems.forEach(item => {
            item.addEventListener('click', function() {
                console.log('Dropdown item clicked!');
                const selectedItem = this.textContent;
                // Handle the selected item
            });
        });
    }

    // Card Body Read More/Read Less
    const readMoreElements = document.querySelectorAll('.read-more');
    if (readMoreElements.length > 0) {
        readMoreElements.forEach(function(element) {
            element.addEventListener('click', function(event) {
                event.preventDefault();
                const cardBody = event.target.closest('.card-body');
                cardBody.querySelector('.short-text').classList.toggle('d-none');
                cardBody.querySelector('.full-text').classList.toggle('d-none');
            });
        });
    }
});