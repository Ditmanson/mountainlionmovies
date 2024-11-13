// Import only the necessary named exports
import { 
    popular_movies, 
    searched_movies, 
    getMovieDetails,
     image_url, 
     fetchData, 
     movie_details_url, 
     credits_url } from './tmdb_data.js';
     
import { 
    postData,
    getCsrfToken,
    postToWatchlist,
    postMovieToMountainMovieDB,
    postSeenMovie,
    postCreditsToMountainMovieDB
 } from './mountainmovie_db.js';

let search_input = document.getElementById('search_input');
let search_button = document.getElementById('search_button');
const resultsDiv = document.getElementById('results');
let search_results = []
let user = '1'

// Initialize the page with Pop1
document.addEventListener('DOMContentLoaded', async () => {
    try {
        user = document.getElementById('user').value;
        console.log('user:', user);
        let pop_movies = await popular_movies();  // Fetch popular movies
        if (Array.isArray(pop_movies)) {
            pop_movies.forEach((movie) => {
                createMovieElement(movie, resultsDiv);
            });
        } else {
            throw new Error("Expected an array of popular movies.");
        }
    } catch (error) {
        console.error("Error in fetching or processing movies:", error);
    }
});

function createMovieElement(movie, container) {
    const movieElement = document.createElement('div');
    movieElement.classList.add('col', 'film-item');

    const poster = movie.poster_path
        ? `${image_url}${movie.poster_path}`
        : 'https://images.unsplash.com/photo-1660922771242-c598e0808188?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c29ycnl8ZW58MHx8MHx8fDA%3D';

    movieElement.innerHTML = `
        <button class="post_movies" value="${movie.id}">
            <img src="${poster}" alt="${movie.title} Poster" class="film-poster">
        </button>
        <h5 class="film-title">${movie.title}</h5>
        <div class="should-post should-post-true">
            <button type="submit" class="m-1 seen btn btn-secondary btn-sm havent-seen-it" value="${movie.id}">Mark as Seen</button>
            <button type="submit" class="m-1 watch-list btn btn-secondary btn-sm remove-from-watchlist" value="${movie.id}">Add to Watchlist</button>
        </div>
    `;

    container.appendChild(movieElement);
}

document.getElementById('search_input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('search_button').click();
    }
});



// Handle search button click
search_button.addEventListener('click', async () => {
    const search_query = document.getElementById('search_input').value;

    // Clear previous search results
    resultsDiv.innerHTML = '';

    if (search_query) {
        try {
            // Fetch the searched movies
            search_results = await searched_movies(search_query);

            if (Array.isArray(search_results)) {
                search_results.forEach((movie) => {
                    createMovieElement(movie, resultsDiv);
                });
            } else {
                throw new Error("Expected an array of search results.");
            }
        } catch (error) {
            console.error("Error in fetching or processing search results:", error);
        }
    } else {
        alert('Please enter a search term.');
    }
});
// Handle Popular button click
document.querySelectorAll('.popular_button').forEach(button => {
    button.addEventListener('click', async () => {
        const popular_page = button.value;  // Get value from the clicked button
        console.log('popular_page:', popular_page);
        // Clear previous search results
        resultsDiv.innerHTML = '';

        if (popular_page) {
            try {
                // Fetch the popular movies
                const search_results = await popular_movies(popular_page);

                if (Array.isArray(search_results)) {
                    search_results.forEach((movie) => {
                        createMovieElement(movie, resultsDiv);
                    });
                } else {
                    throw new Error("Expected an array of search results.");
                }
            } catch (error) {
                console.error("Error in fetching or processing search results:", error);
            }
        }
    });
});
//handle post button click
document.querySelectorAll('.post_movies').forEach(button => {
    button.addEventListener('click', async () => {
        const movieID = button.value;  // Get movie ID from the button's data attribute
        console.log('movieID:', movieID);

        try {
           console.log("i want to make a popup here for movie details...");
        } catch (error) {
            console.error("Error in posting movie data:", error);
        }
    });
});

resultsDiv.addEventListener('click', async (e) => {
    // Log the clicked element for debugging
    console.log('Clicked element:', e.target);

    // Check if the clicked element is a watchlist button
    if (e.target.closest('.watch-list')) {
        const button = e.target.closest('.watch-list');
        const movieID = button.value;
        const user = document.getElementById('user').value;
        console.log('Watchlist button clicked, movieID:', movieID);

        if (button) {
            const parentDiv = button.closest('.should-post');
            console.log('Parent div:', parentDiv);
            if (parentDiv.classList.contains('should-post-true')) {
                parentDiv.classList.remove('should-post-true');
                parentDiv.classList.add('should-post-false');
                try {
                    const film = await getMovieDetails(movieID);
                    const creditData = await fetchData(credits_url(movieID));
                    await postMovieToMountainMovieDB(film);
                    await postCreditsToMountainMovieDB(creditData);
                    console.log("posting");
                }
                catch (error) {
                    console.error("Error in posting movie data:", error);
                }
            } else {
                console.log("should not post");
            }
            // Toggle the class 'add-to-watchlist' and 'remove-from-watchlist'
            if (button.classList.contains('remove-from-watchlist')) {
                button.classList.remove('remove-from-watchlist');
                button.classList.add('added-to-watchlist');
                button.style.backgroundColor = 'green';
                button.innerHTML = "Feature still in development"
                console.log(user, movieID);
                postToWatchlist(user, movieID);
            } else {
                button.classList.remove('added-to-watchlist');
                button.classList.add('remove-from-watchlist');
                button.innerHTML = "You need to wait for sprint 4"
                button.style.backgroundColor = 'red';
            }
        }
        e.stopPropagation();
    }
    
    // Check if the clicked element is a "Seen" button
    else if (e.target.closest('.seen')) {
        const button = e.target.closest('.seen');
        const movieID = button.value;  // Get movie ID from the button's value
        console.log('Seen button clicked, movieID:', movieID);
        
        if (button) {
            const parentDiv = button.closest('.should-post');
            console.log('Parent div:', parentDiv);
            if (parentDiv.classList.contains('should-post-true')) {
                parentDiv.classList.remove('should-post-true');
                parentDiv.classList.remove('should-post-false');
                console.log("posting");
                try {
                    const film = await getMovieDetails(movieID);
                    const creditsData= await fetchData(credits_url(movieID));
                    await postMovieToMountainMovieDB(film);
                    await postCreditsToMountainMovieDB(creditsData);
                    console.log("posting");
                }
                catch (error) {
                    console.error("Error in posting movie data:", error);
                }
            } else {
                console.log("should not post");
            }
            // Toggle seen
            if (button.classList.contains('havent-seen-it')) {
                button.classList.remove('havent-seen-it');
                button.classList.add('seen-it');
                button.style.backgroundColor = 'green';
                button.innerHTML = "Coming in Sprint 4"
                postSeenMovie(user, movieID);
            } else {
                button.classList.remove('seen-it');
                button.classList.add('havent-seen-it');
                button.innerHTML = "Chill I'll get to it"
                button.style.backgroundColor = 'red';
            }
        }
        e.stopPropagation();
    }
});
