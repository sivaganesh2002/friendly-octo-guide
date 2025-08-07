document.addEventListener('DOMContentLoaded', function() {
    const welcomeOverlay = document.querySelector('.welcome-message-overlay');
    if (welcomeOverlay) {
        setTimeout(() => {
            // Fade out the message
            welcomeOverlay.style.opacity = '0';
            // Remove it after the fade transition
            setTimeout(() => {
                welcomeOverlay.style.display = 'none';
            }, 500); // Match CSS transition time
        }, 3000); // 3 seconds
    }
});