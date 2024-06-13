
// wait for the DOM to be loaded
document.addEventListener('DOMContentLoaded', function() {
// get the 3 buttons
    console.log('DOM loaded')
    const darkButton = document.getElementById('bt-dark');
    const lightButton = document.getElementById('bt-light');
    const autoButton = document.getElementById('bt-auto');

    // check if there is a saved theme preference in localStorage
    const savedTheme = localStorage.getItem('theme');

    // apply the saved theme if it exists
    if (savedTheme) {
        document.documentElement.classList.add(savedTheme);
    }
    if (darkButton) {
        // if the button is clicked, set the class in localStorage
        darkButton.addEventListener('click', function() {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            
            console.log('dark');
        });
    }

    if (lightButton) {
        lightButton.addEventListener('click', function() {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            console.log('light');
        });
    }

    if (autoButton) {
        autoButton.addEventListener('click', function() {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'auto');
            console.log('auto');
        });
    }
});
