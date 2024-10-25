// in compare_movies.html when you click more info button, the description & release date will appear
document.getElementById('more-info-icon').addEventListener('click', function() {
    var overviewSection = document.getElementById('overview-section');
    if (overviewSection.style.display === 'none') {
        overviewSection.style.display = 'flex';  // Make it a flex container to align nicely
    } else {
        overviewSection.style.display = 'none';
    }
});