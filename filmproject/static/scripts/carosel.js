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
    console.log("DOM fully loaded and parsed. Starting to fetch data...");

    const baseUrl = 'https://image.tmdb.org/t/p/w500'; // Base URL for TMDB images

    // Fetch watchlist films and dynamically load them
    const fetchWatchlist = () => {
        console.log("Fetching watchlist data...");
        fetch('/api/user/watchlist/')
            .then(response => {
                if (!response.ok) {
                    console.error("Failed to fetch watchlist data. Status:", response.status);
                    return;
                }
                return response.json();
            })
            .then(data => {
                if (data && data.length > 0) {
                    console.log("Watchlist data fetched successfully:", data);
                    fetchMovieDetailsFromTMDB(data, 'watchlist', 'watchlistCarousel');
                } else {
                    console.log("No watchlist data available.");
                }
            })
            .catch(error => console.error('Error fetching watchlist:', error));
    };

    // Fetch seen films and dynamically load them
    const fetchSeenFilms = () => {
        console.log("Fetching seen films data...");
        fetch('/api/user/seen_films/')
            .then(response => {
                if (!response.ok) {
                    console.error("Failed to fetch seen films data. Status:", response.status);
                    return;
                }
                return response.json();
            })
            .then(data => {
                if (data && data.length > 0) {
                    console.log("Seen films data fetched successfully:", data);
                    fetchMovieDetailsFromTMDB(data, 'seenFilms', 'seenFilmsCarousel');
                } else {
                    console.log("No seen films data available.");
                }
            })
            .catch(error => console.error('Error fetching seen films:', error));
    };

    // Fetch movie details from TMDB based on tmdb_id
const fetchMovieDetailsFromTMDB = (movies, elementId, carouselId) => {
    const promises = movies.map((movie) => {
        // Access the correct tmdb_id inside the nested film object
        const tmdbId = movie.film.tmdb_id;  // Correctly reference movie.film.tmdb_id
        const tmdbUrl = `https://api.themoviedb.org/3/movie/${tmdbId}`;
        
        return fetch(tmdbUrl, options)
            .then(response => {
                if (!response.ok) {
                    console.error(`Failed to fetch TMDB data for movie ID ${tmdbId}`);
                    return null;
                }
                return response.json();
            })
            .then(film => {
                if (film) {
                    // Merge the TMDb data with the existing movie data
                    return {
                        ...movie.film,  // Keep the film properties from the backend
                        title: film.title,
                        poster_path: film.poster_path,
                        overview: film.overview,
                        vote_average: film.vote_average
                    };
                }
                return null;
            })
            .catch(error => {
                console.error(`Error fetching TMDB data for movie ID ${tmdbId}:`, error);
                return null;
            });
    });

    // After all movie details are fetched, populate the carousel
    Promise.all(promises).then((moviesWithDetails) => {
        const validMovies = moviesWithDetails.filter(movie => movie !== null);
        if (validMovies.length > 0) {
            populateCarousel(validMovies, elementId, carouselId);
        } else {
            console.error("No valid movies to display in the carousel.");
        }
    });
};

    // Function to populate the carousel dynamically
    const populateCarousel = (films, elementId, carouselId) => {
        console.log(`Populating carousel for element: ${elementId}, carousel: ${carouselId}`);
        
        const container = document.getElementById(elementId);
        if (!container) {
            console.error(`Element with ID "${elementId}" not found.`);
            return;
        }

        // Clear previous carousel content
        container.innerHTML = '';
        console.log(`Carousel content cleared for element: ${elementId}`);

        // Dynamically create carousel items
        films.forEach((film, index) => {
            console.log(`Full film data for "${film.title}":`, film);  // Log full film data for debugging

            const movieElement = document.createElement('div');
            movieElement.classList.add('carousel-item');

            // Ensure first element is active
            if (index === 0) {
                movieElement.classList.add('active');
                console.log(`First element (index 0) set as active for carousel: ${carouselId}`);
            }

            // Check the poster path and log it
            const posterPath = film.poster_path ? `${baseUrl}${film.poster_path}` : 'default_poster_url_here';
            console.log(`Poster path for film "${film.title}": ${posterPath}`);

            // Insert the poster and description
            movieElement.innerHTML = `
                <img src="${posterPath}" class="d-block w-100 img-fluid" alt="${film.title}" style="max-height: 500px;">
                <div class="carousel-caption d-none d-md-block">
                    <h5>${film.title}</h5>
                    <p>${film.overview}</p>
                    <p>Rating: ${film.vote_average}</p>
                </div>
            `;

            container.appendChild(movieElement);
        });

        console.log(`Carousel populated for element: ${elementId}. Reinitializing...`);
        initializeBootstrapCarousel(carouselId);
    };

    // Manually initialize or reset Bootstrap carousel
    const initializeBootstrapCarousel = (carouselId) => {
        console.log(`Initializing/reinitializing Bootstrap carousel with ID: ${carouselId}`);
        const carouselElement = document.getElementById(carouselId);
        if (carouselElement) {
            const carouselInstance = bootstrap.Carousel.getInstance(carouselElement);
            if (carouselInstance) {
                console.log(`Disposing of existing Bootstrap carousel instance for ID: ${carouselId}`);
                carouselInstance.dispose();  // Reset if already initialized
            }
            new bootstrap.Carousel(carouselElement);  // Reinitialize with new items
            console.log(`Bootstrap carousel reinitialized for ID: ${carouselId}`);
        } else {
            console.error(`No carousel element found with ID: ${carouselId}`);
        }
    };

    // Fetch and populate the carousels on page load
    console.log("Fetching carousels...");
    fetchWatchlist();
    fetchSeenFilms();
});
