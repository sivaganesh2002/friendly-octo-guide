document.addEventListener('DOMContentLoaded', () => {
    // --- Element Selection ---
    const searchBar = document.getElementById('search-bar');
    const problems = document.querySelectorAll('ul > li');
    const tags = document.querySelectorAll('.tag');

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

    // Event listener for search bar
    searchBar.addEventListener('input', updateProblemVisibility);
});