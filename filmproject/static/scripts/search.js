// Import only the necessary named exports
import { search_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData, getCsrfToken } from './post_mountainmovie_db.js';


let search_input = document.getElementById('search_input');
let search_button = document.getElementById('search_button');
let movie_title0 = document.getElementById('movie_title0');
let movie_poster0 = document.getElementById('movie_poster0');
const resultsDiv = document.getElementById('results');

document.addEventListener('DOMContentLoaded', async () => {
    try {
        let pop_movies = await popular_movies();  // Fetch popular movies
        // Make sure `pop_movies` is an array
        if (!Array.isArray(pop_movies)) {
            throw new Error("Expected an array of movies.");
        }

        // Iterate over the movies array with movie object
        for (const movie of pop_movies) {
            console.log("Movie:", movie);
            const movieElement = document.createElement('div');
            movieElement.classList.add('col', 'film-item');
            const poster = movie.poster_path ? `${image_url}${movie.poster_path}` : 'https://images.unsplash.com/photo-1660922771242-c598e0808188?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8c29ycnl8ZW58MHx8MHx8fDA%3D';
            movieElement.innerHTML = `
                <a href="/films/">
                    <img src="${poster}" alt="${movie.title} Poster" class="film-poster">
                </a>
            <h5 class="film-title">${movie.title}</h5>
            <button type="submit" class="btn btn-success btn-sm add-to-seen">Mark as Seen</button>
            <button type="submit" class="btn btn-secondary btn-sm add-to-watchlist">Add to Watchlist</button>
            `;
            const resultsDiv = document.getElementById('results'); // Make sure this element exists in your HTML
            resultsDiv.appendChild(movieElement);
        }
    } catch (error) {
        console.error("Error in fetching or processing movies:", error);
    }
});

let popular_movies = async () => {
    const data = await fetchData(pop_url('1'));
    console.log('data:', data.results);
    return data.results;
};
let searched_movies = async (query) => {
    const data = await fetchData(search_url(query));
    console.log('data:', data.results);
    return data.results;
};