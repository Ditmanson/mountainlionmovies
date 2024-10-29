import './fetch_tmdb_data.js';
import './post_mountainmovie_db.js';
import { credits_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData } from './post_mountainmovie_db.js';
import { getData, getCsrfToken, apiEndpoint } from './get_mountain_movie_db.js';

document.addEventListener('DOMContentLoaded', () => {
    //initialize    
    let movie_ids = [];
    let movie_button_1 = document.getElementById('movie1id');
    let movie_button_2 = document.getElementById('movie2id');
    let movieImage1 = movie_button_1.querySelector('img'); // Get the image element for movie 1
    let movieImage2 = movie_button_2.querySelector('img'); // Get the image element for movie 2
    let movies = [];
    //helper functions
    const getRandomIndex = (some_array) => {
        return Math.floor(Math.random() * some_array.length);
    };

    // Fetch the data
    getData(apiEndpoint('seen_films')).then(data => {
        movie_ids = data.map(movie => movie.film.id);
        movies = data.map(film => film.film);
        console.log('movies:', movies);

        // Map the movie IDs to the movie_ids array
        console.log('movie_ids:', movie_ids);
        console.log('movie_ids.length:', movie_ids.length);

        // Only proceed if there are movie_ids in the array
        if (movie_ids.length > 0) {
            console.log('movie_ids.length:', movie_ids.length);
        } else {
            console.log('No movie_ids found.');
        }
        let randomMovieID = getRandomIndex(movie_ids);
        console.log(`random movie  ${movies[randomMovieID]}`);

        movie_button_1.addEventListener('click', () => {
            randomMovieID = getRandomIndex(movie_ids);
            movieImage1.src = `https://image.tmdb.org/t/p/w300/${movie_ids[randomMovieID].poster_path}`;
            console.log(`random movie id: ${movie_ids[randomMovieID]}`);
            console.log('movie1id clicked');

        });

        movie_button_2.addEventListener('click', () => {
            randomMovieID = getRandomIndex(movie_ids);
            console.log(`random movie id: ${movie_ids[randomMovieID]}`);
            console.log('movie2id clicked');
        });


    }).catch(error => {
        console.error('Error fetching movies:', error);
    });
});
