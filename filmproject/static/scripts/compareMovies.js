document.addEventListener('DOMContentLoaded', () => {
    loadNewMovies();

    async function loadNewMovies() {
        try {
            const response = await fetch('/api/get_comparison_movies/');
            if (!response.ok) throw new Error('Failed to fetch movies');

            const data = await response.json();
            displayMovies(data.movie1, data.movie2);
        } catch (error) {
            console.error('Error loading movies:', error);
        }
    }

    function displayMovies(movie1, movie2) {
        document.getElementById('movie1-title').textContent = movie1.title;
        document.getElementById('movie2-title').textContent = movie2.title;
        document.getElementById('movie1-img').src = `https://image.tmdb.org/t/p/w300/${movie1.poster_path}`;
        document.getElementById('movie2-img').src = `https://image.tmdb.org/t/p/w300/${movie2.poster_path}`;

        document.querySelector('.movie1-button').setAttribute('data-movie-id', movie1.id);
        document.querySelector('.movie2-button').setAttribute('data-movie-id', movie2.id);

        addSelectionListeners(movie1.id, movie2.id);
    }

    function addSelectionListeners(movie1Id, movie2Id) {
        document.querySelectorAll('.movie-selection-button').forEach(button => {
            button.addEventListener('click', async (event) => {
                event.preventDefault();
                const selectedMovieId = event.currentTarget.getAttribute('data-movie-id');

                const body = JSON.stringify({
                    selected_movie: selectedMovieId,
                    movie1_id: movie1Id,
                    movie2_id: movie2Id
                });

                try {
                    const response = await fetch('/api/submit_movie_selection/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: body
                    });

                    if (!response.ok) throw new Error('Failed to submit selection');

                    const result = await response.json();
                    if (result.success) {
                        loadNewMovies();
                    } else {
                        console.error('Submission error:', result.error);
                    }
                } catch (error) {
                    console.error('Error submitting selection:', error);
                }
            });
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});


// This is the old entirety of compareMovies.js:
// in compare_movies.html when you click more info button, the description & release date will appear
// document.getElementById('more-info-icon').addEventListener('click', function() {
//     var overviewSection = document.getElementById('overview-section');
//     if (overviewSection.style.display === 'none') {
//         overviewSection.style.display = 'flex';  // Make it a flex container to align nicely
//     } else {
//         overviewSection.style.display = 'none';
//     }
// });