document.addEventListener('DOMContentLoaded', () => {
    // --- Element Selection ---
    const searchBar = document.getElementById('search-bar');
    const difficultyFilter = document.getElementById('difficulty-filter');
    const sortButton = document.getElementById('sort-difficulty');
    const problemList = document.querySelector('ul');
    const problems = document.querySelectorAll('ul > li');
    const tags = document.querySelectorAll('div.tags span'); // More specific selector for tags

    // --- Tag Highlighting ---
    tags.forEach(tag => {
        tag.addEventListener('mouseover', () => {
            tag.style.color = 'rgba(19, 14, 14, 0.86)';
            tag.style.fontWeight = 'bold';
        });
        tag.addEventListener('mouseout', () => {
            tag.style.color = 'rgba(76, 76, 76, 0.86)';
            tag.style.fontWeight = 'normal';
        });
    });

    // --- Combined Filter and Search Function ---
    const updateProblemVisibility = () => {
        const searchQuery = searchBar.value.toLowerCase();
        const difficultyValue = difficultyFilter.value.toLowerCase();

        problems.forEach(problem => {
            const title = problem.querySelector('a').textContent.toLowerCase();
            
            // CORRECTED: Select the last span in the li, which is the difficulty
            const difficultySpan = problem.querySelector('span:last-child');
            const difficulty = difficultySpan.textContent.toLowerCase().trim();

            // Check if the problem matches both the search query and the difficulty filter
            const matchesSearch = title.includes(searchQuery);
            const matchesDifficulty = (difficultyValue === 'all' || difficulty === difficultyValue);

            if (matchesSearch && matchesDifficulty) {
                problem.style.display = 'flex';
            } else {
                problem.style.display = 'none';
            }
        });
    };

    // --- Event Listeners ---
    searchBar.addEventListener('input', updateProblemVisibility);
    difficultyFilter.addEventListener('change', updateProblemVisibility);

    // --- Sorting ---
    sortButton.addEventListener('click', () => {
        const problemsArray = Array.from(problemList.children);
        
        // CORRECTED: Define a logical order for sorting
        const difficultyOrder = { 'easy': 1, 'medium': 2, 'hard': 3 };

        problemsArray.sort((a, b) => {
            // CORRECTED: Select the last span to get the correct difficulty text
            const difficultyA = a.querySelector('span:last-child').textContent.toLowerCase().trim();
            const difficultyB = b.querySelector('span:last-child').textContent.toLowerCase().trim();

            // Use the order map for sorting, falling back to 0 for unknown values
            const orderA = difficultyOrder[difficultyA] || 0;
            const orderB = difficultyOrder[difficultyB] || 0;

            return orderA - orderB;
        });

        // Re-append the sorted elements to the list
        problemsArray.forEach(problem => problemList.appendChild(problem));
    });
});