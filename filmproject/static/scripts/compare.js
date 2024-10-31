import './fetch_tmdb_data.js';
import './post_mountainmovie_db.js';
import { credits_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData } from './post_mountainmovie_db.js';
import { getData, getCsrfToken, apiEndpoint } from './get_mountain_movie_db.js';

document.addEventListener('DOMContentLoaded', () => {
    //initialize    
    let movie_ids = [];
    let movie_button_1 = document.getElementById('movie1button');
    let movieImage1 = movie_button_1.querySelector('img'); // Get the image element for movie 1
    let movie1_title = document.getElementById('movie1_title');
    let movie1_release_date = document.getElementById('movie1_release_date');
    let movie1_overview = document.getElementById('movie1_overview');
    let movie1id = document.getElementById('movie1id');


    let movie_button_2 = document.getElementById('movie2button');
    let movie2_title = document.getElementById('movie2_title');
    let movieImage2 = movie_button_2.querySelector('img'); // Get the image element for movie 2
    let movie2_release_date = document.getElementById('movie2_release_date');
    let movie2_overview = document.getElementById('movie2_overview');
    let movie2id = document.getElementById('movie2id');

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
            //post movie goes here
            console.log('clicked movie 1');
            postData({
                viewer: 1,
                film_a: movie1id.value,
                film_b: movie2id.value,
                date: null,
                a_points: 1,
                b_points: 0,
            }, 'viewer_ratings');


            randomMovieID = getRandomIndex(movie_ids);
            movieImage1.src = `https://image.tmdb.org/t/p/w300/${movies[randomMovieID].poster_path}`;
            movie1_title.innerText = movies[randomMovieID].title;
            movie1_release_date.innerText = movies[randomMovieID].release_date;
            movie1_overview.innerText = movies[randomMovieID].overview;
            movie1id.value = movies[randomMovieID].id;

        });

        movie_button_2.addEventListener('click', () => {
            //post movie goes here
            console.log('clicked movie 2');
            postData({
                viewer: 1,
                film_a: movie1id.value,
                film_b: movie2id.value,
                date: null,
                a_points: 0,
                b_points: 1,
            }, 'viewer_ratings');

            randomMovieID = getRandomIndex(movie_ids);
            movieImage2.src = `https://image.tmdb.org/t/p/w300/${movies[randomMovieID].poster_path}`;
            movie2_title.innerText = movies[randomMovieID].title;
            movie2_release_date.innerText = movies[randomMovieID].release_date;
            movie2_overview.innerText = movies[randomMovieID].overview;
            movie2id.value = movies[randomMovieID].id;
        });


    }).catch(error => {
        console.error('Error fetching movies:', error);
    });
});
