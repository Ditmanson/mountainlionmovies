/**
 * TMDB API configuration
 */
const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyODY2NjUyMi4xNDkxNjMsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._nORPBk_Vz0YNM_Rav4nMW5_x2d92IbmXaXjNy_ObEc'
    }
};

document.addEventListener("DOMContentLoaded", function () {
    const baseUrl = 'https://image.tmdb.org/t/p/w500'; // Base URL for TMDB images

    // Function to fetch and display watchlist films for the current user
    const fetchWatchlist = () => {
        fetch('/api/user/watchlist/')
            .then(response => response.json())
            .then(data => {
                console.log("Watchlist API Response:", data);  // Debugging
                if (data.length > 0) {
                    console.log("Populating Watchlist Carousel");
                    data.forEach(filmData => {
                        fetchFilmFromTMDB(filmData.film.tmdb_id, 'watchlist');
                    });
                } else {
                    console.log("No watchlist data available.");
                }
            })
            .catch(error => console.error('Error fetching watchlist:', error));
    };

    // Function to fetch and display seen films for the current user
    const fetchSeenFilms = () => {
        fetch('/api/user/seen_films/')
            .then(response => response.json())
            .then(data => {
                console.log("Seen Films API Response:", data);  // Debugging
                if (data.length > 0) {
                    console.log("Populating Seen Films Carousel");
                    data.forEach(filmData => {
                        fetchFilmFromTMDB(filmData.film.tmdb_id, 'seenFilms');
                    });
                } else {
                    console.log("No seen films data available.");
                }
            })
            .catch(error => console.error('Error fetching seen films:', error));
    };

    // Function to fetch film data from TMDB using tmdb_id
    const fetchFilmFromTMDB = (tmdbId, elementId) => {
        const tmdbUrl = `https://api.themoviedb.org/3/movie/${tmdbId}`;
        fetch(tmdbUrl, options)
            .then(response => response.json())
            .then(film => {
                console.log("Fetched Film from TMDB:", film);
                populateCarousel([film], elementId);
            })
            .catch(error => console.error(`Error fetching film from TMDB for ID ${tmdbId}:`, error));
    };

    const populateCarousel = (films, elementId) => {
        const container = document.getElementById(elementId);
        if (!container) {
            console.error(`Element with ID "${elementId}" not found.`);
            return;  // Exit the function if the element is not found
        }
        container.innerHTML = ''; // Clear previous content
    
        if (films.length > 0) {
            films.forEach((film, index) => {
                console.log("Processing Film:", film.title);  // Debugging
    
                const movieElement = document.createElement('div');
                movieElement.classList.add('carousel-item'); // Always add 'carousel-item'
    
                // Add 'active' class only if it's the first element (index 0)
                if (index === 0) {
                    movieElement.classList.add('active');
                }
    
                // Safely check if the poster path exists before sending requests to TMDB
                const posterPath = film.poster_path ? `${baseUrl}${film.poster_path}` : 'default_poster_url_here';
    
                movieElement.innerHTML = `
                    <img src="${posterPath}" class="d-block w-100 img-fluid" alt="${film.title}" 
                    style="max-height: 500px; width: auto; max-width: 50%; margin: 10 auto;">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>${film.title}</h5>
                        <p>${film.overview}</p>
                        <p>Rating: ${film.vote_average}</p>
                    </div>
                `;
                container.appendChild(movieElement);
            });
        } else {
            console.log(`No films found for element ${elementId}`);
            container.innerHTML = '<p>No movies found.</p>';
        }
    };
    
    

    // Fetch the data when the page loads
    fetchWatchlist();
    fetchSeenFilms();
});
