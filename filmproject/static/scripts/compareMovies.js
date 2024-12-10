document.addEventListener('DOMContentLoaded', () => {
    // Toggle overview section visibility
    document.getElementById('more-info-icon').addEventListener('click', function() {
        const overviewSection = document.getElementById('overview-section');
        overviewSection.style.display = (overviewSection.style.display === 'none') ? 'flex' : 'none';
    });

    // Fetch CSRF token
    const getCsrfToken = () => {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken='));
        return cookieValue ? cookieValue.split('=')[1] : '';
    };

    // Elements for movie buttons and metadata
    const movie1Button = document.getElementById('movie1button');
    const movie2Button = document.getElementById('movie2button');
    const cantDecideButton = document.getElementById('cant-decide-button');
    let movie1Id = document.getElementById('movie1id').value;
    let movie2Id = document.getElementById('movie2id').value;

    const submitComparison = (selectedMovieId) => {
        const data = {
            selected_movie: selectedMovieId,
            movie1_id: movie1Id,
            movie2_id: movie2Id,
        };

        // Debugging output: log the data being sent
        console.log("Submitting comparison with data:", data);

        fetch('/compare_movies/submit_selection/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(JSON.stringify(err)) });
            }
            return response.json();
        })
        .then(data => {
            console.log('Comparison submitted successfully:', data);
            return fetchNewMovies();  // Fetch new movies on success
        })
        .catch(error => console.error('Error submitting comparison:', error));
    };

    // Fetch new movies after each comparison
    const fetchNewMovies = () => {
        fetch('/compare_movies/', {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',  // Signal that this is an AJAX request
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch new movies');
            }
            return response.json();
        })
        .then(data => {
            // Update the movie details with new movies
            movie1Id = data.movie1.id;
            movie2Id = data.movie2.id;

            document.getElementById('movie1_title').innerText = data.movie1.title;
            document.getElementById('movie1img').src = data.movie1.poster_path;
            document.getElementById('movie1_overview').innerText = data.movie1.overview;

            document.getElementById('movie2_title').innerText = data.movie2.title;
            document.getElementById('movie2img').src = data.movie2.poster_path;
            document.getElementById('movie2_overview').innerText = data.movie2.overview;
        })
        .catch(error => console.error('Error fetching new movies:', error));
    };

    // Event listeners for movie selections
    movie1Button.addEventListener('click', () => submitComparison(movie1Id));
    movie2Button.addEventListener('click', () => submitComparison(movie2Id));

    // Event listener for "can't decide" button
    cantDecideButton.addEventListener('click', () => submitComparison("can't_decide"));
});