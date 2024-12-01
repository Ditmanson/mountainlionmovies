// Function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    const darkModeSwitch = document.getElementById('darkModeSwitch');
    const isDarkModeEnabled = localStorage.getItem('darkModeEnabled') === 'true';

    // Toggle the dark mode class on the body
    body.classList.toggle('dark-mode', !isDarkModeEnabled);

    // Update the switch state
    darkModeSwitch.checked = !isDarkModeEnabled;

    // Store the user's preference in localStorage
    localStorage.setItem('darkModeEnabled', !isDarkModeEnabled);
}

// Check the user's preference on page load and apply the dark mode if enabled
document.addEventListener('DOMContentLoaded', function () {
    const isDarkModeEnabled = localStorage.getItem('darkModeEnabled') === 'true';
    const darkModeSwitch = document.getElementById('darkModeSwitch');

    if (isDarkModeEnabled) {
        document.body.classList.add('dark-mode');
    }

    // Set the switch to the correct state on page load
    if (darkModeSwitch) {
        darkModeSwitch.checked = isDarkModeEnabled;
        darkModeSwitch.addEventListener('change', toggleDarkMode);
    }
});