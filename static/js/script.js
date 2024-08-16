document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const searchResultsContainer = document.getElementById('search-results');
    const dropdownList = document.getElementById('dropdown-list');

    // Search Bar
    if (searchBtn && searchInput && searchResultsContainer) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const searchTerm = searchInput.value.trim();
            if (searchTerm) {
                fetch(`/search?q=${searchTerm}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Error fetching search results');
                        }
                        return response.json();
                    })
                    .then(posts => {
                        searchResultsContainer.innerHTML = '';
                        if (posts.length === 0) {
                            searchResultsContainer.innerHTML = '<p>No results found.</p>';
                        } else {
                            posts.forEach(post => {
                                const postHTML = `
                                    <h2>${post.title}</h2>
                                    <p>${post.content}</p>
                                `;
                                searchResultsContainer.innerHTML += postHTML;
                            });
                        }
                    })
                    .catch(error => {
                        console.error(error);
                        window.location.href = '/404.html';
                    });
            }
        });
    }

    // Dropdown List Items
    if (dropdownList) {  // Ensure the dropdownList exists before adding an event listener
        dropdownList.addEventListener('click', (e) => {
            if (e.target && e.target.classList.contains('dropdown-item')) {
                console.log('Dropdown item clicked!');
                // Handle the selected item here
                // The selectedItem variable was removed since it's not used
            }
        });
    }

    // Card Body Read More/Read Less
    const readMoreElements = document.querySelectorAll('.read-more');
    if (readMoreElements.length > 0) {
        readMoreElements.forEach(element => {
            element.addEventListener('click', (event) => {
                event.preventDefault();
                const cardBody = event.target.closest('.card-body'); // This is now used within the function scope
                const shortText = cardBody.querySelector('.short-text');
                const fullText = cardBody.querySelector('.full-text');
                
                if (shortText && fullText) {
                    shortText.classList.toggle('d-none');
                    fullText.classList.toggle('d-none');
                }
            });
        });
    }
});