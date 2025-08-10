document.addEventListener('DOMContentLoaded', () => {
    const menuText = document.getElementById('menu-text');
    const menuIconOnly = document.getElementById('menu-icon-only');
    const userName = document.getElementById('user-name');

    // Check if user is authenticated and on the '/' URL
    const isAuthenticated = document.body.dataset.isAuthenticated === 'true';
    const isHomePage = document.body.dataset.isHomePage === 'true';

    if (isAuthenticated && isHomePage) {
        setTimeout(() => {
            menuText.style.display = 'none';
            menuIconOnly.style.display = 'inline-flex';
        }, 3000); // Replace after 3 seconds
    }
});