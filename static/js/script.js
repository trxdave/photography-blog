const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');
const searchResultsContainer = document.getElementById('search-results');
const dropdownList = document.getElementById('dropdown-list');

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

// Add dropdown list items
const dropdownItems = document.querySelectorAll('.dropdown-item');
dropdownItems.forEach(item => {
    item.addEventListener('click', function() {
      console.log('Dropdown item clicked!');
      const selectedItem = this.textContent;
      //...
    });
  });