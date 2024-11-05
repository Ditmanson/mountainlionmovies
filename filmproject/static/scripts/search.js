// Import only the necessary named exports
import { credits_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData, getCsrfToken } from './post_mountainmovie_db.js';


let search_input = document.getElementById('search_input');
let search_button = document.getElementById('search_button');
let movie_title0 = document.getElementById('movie_title0');
let movie_poster0 = document.getElementById('movie_poster0');

document.addEventListener('DOMContentLoaded', async () => {
    try {
        let pop_movies = await popular_movies();  // Fetch popular movies

        // Make sure `pop_movies` is an array
        if (!Array.isArray(pop_movies)) {
            throw new Error("Expected an array of movies.");
        }

        console.log("Fetched movies:", pop_movies);

        // Iterate over the movies array with index and movie object
        for (const [index, movie] of pop_movies.entries()) {
            console.log(`Index: ${index}, Movie:`, movie);

            // Get movie title and poster elements by their dynamic ID
            let movie_title = document.getElementById(`movie_title${index}`);
            let movie_poster = document.getElementById(`movie_poster${index}`);

            // If the movie title element exists, update its innerHTML
            if (movie_title) {
                movie_title.innerHTML = movie.title;
            } else {
                console.error(`Movie title element not found for index ${index}`);
            }

            // If the movie poster element exists, update its src
            if (movie_poster) {
                movie_poster.src = `${image_url}${movie.poster_path}`;
            } else {
                console.error(`Movie poster element not found for index ${index}`);
            }
        }
    } catch (error) {
        console.error("Error in fetching or processing movies:", error);
    }
});


// let popular_movies = async () => {
//     const data = await fetchData(pop_url('1'));
//     console.log('data:', data);
//     // display_results(data);
// };


// search_button.addEventListener('click', async () => {
//     const query = search_input.value;
//     const data = await fetchData(pop_url(query));
//     console.log('data:', data);
//     display_results(data);
// });

let popular_movies = async () => {
    const data = await fetchData(pop_url('1'));
    console.log('data:', data.results);
    return data.results;
    // display_results(data);
};