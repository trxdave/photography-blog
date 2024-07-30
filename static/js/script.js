const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');
const searchResultsContainer = document.getElementById('search-results');

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

// Add event listener to dropdown list items
const dropdownItems = document.querySelectorAll('.dropdown-item');
dropdownItems.forEach(item => {
  item.addEventListener('click', function() {
    const selectedItem = this.textContent;
    // Update search input with selected item
    searchInput.value = selectedItem;
    // Close dropdown menu
    dropdownList.classList.remove('show');
  });
});