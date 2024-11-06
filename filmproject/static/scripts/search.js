// Import only the necessary named exports
import { search_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData, getCsrfToken } from './post_mountainmovie_db.js';

let search_input = document.getElementById('search_input');
let search_button = document.getElementById('search_button');
const resultsDiv = document.getElementById('results');
let search_results = []

// Wait for DOM content to be loaded
document.addEventListener('DOMContentLoaded', async () => {
    try {
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

// Function to fetch popular movies
let popular_movies = async () => {
    const data = await fetchData(pop_url('1'));
    console.log('Fetched popular movies:', data.results);
    return data.results;
};

// Function to fetch searched movies
let searched_movies = async (query) => {
    const data = await fetchData(search_url(query));
    console.log('Fetched searched movies:', data.results);
    return data.results;
};

function createMovieElement(movie, container) {
    const movieElement = document.createElement('div');
    movieElement.classList.add('col', 'film-item');

    const poster = movie.poster_path
        ? `${image_url}${movie.poster_path}`
        : 'https://images.unsplash.com/photo-1660922771242-c598e0808188?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c29ycnl8ZW58MHx8MHx8fDA%3D';

    movieElement.innerHTML = `
        <a href="/films/${movie.id}">
            <img src="${poster}" alt="${movie.title} Poster" class="film-poster">
        </a>
        <h5 class="film-title">${movie.title}</h5>
        <button type="submit" class="btn btn-success btn-sm add-to-seen">Mark as Seen</button>
        <button type="submit" class="btn btn-secondary btn-sm add-to-watchlist">Add to Watchlist</button>
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
document.getElementById('search_button').addEventListener('click', async () => {
    const search_query = document.getElementById('search_input').value.trim();

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
