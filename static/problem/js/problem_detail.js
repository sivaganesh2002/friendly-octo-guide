document.addEventListener("DOMContentLoaded", () => {
    const testcaseButton = document.getElementById("ctestcase-btn");

    if (testcaseButton) {
        const svgIcon = `
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16">
                <rect y="4" width="20" height="2" rx="1"></rect>
                <rect y="11" width="20" height="2" rx="1"></rect>
                <rect y="18" width="20" height="2" rx="1"></rect>
            </svg>
        `;
        testcaseButton.querySelector(".svg-icon").innerHTML = svgIcon;
    }
});