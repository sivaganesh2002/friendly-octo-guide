document.addEventListener('DOMContentLoaded', () => {
    // --- Element Selection ---
    const searchBar = document.getElementById('search-bar');
    const problems = document.querySelectorAll('ul > li');
    const tags = document.querySelectorAll('.tag');
    const searchIcon = document.getElementById('search-icon');

    // --- Tag Highlighting ---

    // --- Search Function ---
    const updateProblemVisibility = () => {
        const searchQuery = searchBar.value.toLowerCase();

        problems.forEach(problem => {
            const title = problem.querySelector('a').textContent.toLowerCase();
            const matchesSearch = title.includes(searchQuery);

            if (matchesSearch) {
                problem.style.display = 'flex';
            } else {
                problem.style.display = 'none';
            }
        });
    };

    searchIcon.addEventListener('click', () => {
        searchBar.classList.add('visible'); // Add the visible class for transition
        searchBar.style.display = 'block'; // Ensure the search bar is displayed
        searchBar.focus(); // Focus the search bar
        searchIcon.style.opacity = '0'; // Fade out the search icon
        setTimeout(() => {
            searchIcon.style.display = 'none'; // Hide the search icon after transition
        }, 500); // Match the transition duration
    });

    // --- Hide Search Bar on Blur ---
    searchBar.addEventListener('blur', () => {
        searchBar.classList.remove('visible'); // Remove the visible class for transition
        searchIcon.style.display = 'block'; // Show the search icon
        setTimeout(() => {
            searchIcon.style.opacity = '1'; // Fade in the search icon
            searchBar.style.display = 'none'; // Hide the search bar after transition
        }, 500); // Match the transition duration
    });
});