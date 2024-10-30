// Import only the necessary named exports
import { search_url, pop_url, image_url, fetchData, movie_details_url, credits_url } from './fetch_tmdb_data.js';
import { postData, getCsrfToken } from './post_mountainmovie_db.js';

let search_input = document.getElementById('search_input');
let search_button = document.getElementById('search_button');
const resultsDiv = document.getElementById('results');
let search_results = []

// Initialize the page with Pop1
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
const popular_movies = async (number = '1') => {
    const data = await fetchData(pop_url(number));
    console.log('Fetched popular movies:', data.results);
    return data.results;
};

// Function to fetch searched movies
const searched_movies = async (query) => {
    const data = await fetchData(search_url(query));
    console.log('Fetched searched movies:', data.results);
    return data.results;
};

// Function to get Movie Details
const getMovieDetails = async (movieID) => {
    const data = await fetchData(movie_details_url(movieID));
    console.log('Fetched movie details:', data);
    return data;
};

// Function to get cast and crew
const getMovieCredits = async (movieID) => {
    const data = await fetchData(credits_url(movieID));
    console.log('Fetched movie credits:', data);
    return data;
};

// Function Post to MountainMovie DB
const postToMountainMovieDB = async (movie) => {
    const post = await postData({
        id: movie.id,
        adult: movie.adult,
        backdrop_path: movie.backdrop_path,
        belongs_to_collection: false,
        budget: movie.budget || 0,
        homepage: movie.homepage || '',
        imdb_id: movie.imdb_id || '',
        original_title: movie.original_title,
        overview: movie.overview,
        popularity: movie.popularity,
        poster_path: movie.poster_path,
        release_date: movie.release_date,
        revenue: movie.revenue || 0,
        runtime: movie.runtime || 0,
        status: movie.status || '',
        tagline: movie.tagline || '',
        title: movie.title,
        tmdb_id: movie.id,
        vote_average: movie.vote_average,
        vote_count: movie.vote_count
    }, 'films');
    console.log('Posted to MountainMovie DB:', post);
};

// Function to post cast and crew
const postCreditsToMountainMovieDB = async (movieID) => {
    const creditResponse = await fetchData(credits_url(movieID));
    console.log('Fetched movie credits:', creditResponse);
    //cast
    for (const cast of creditResponse.cast) {
        console.log('Posting cast data:', cast);
        await postData({
            id: cast.id,
            adult: cast.adult || false,
            gender: cast.gender || 2,
            tmdb_id: cast.id || 0,
            known_for_department: 'acting',
            name: cast.name || '',
            popularity: cast.popularity || 0,
            profile_path: cast.profile_path || '',
        }, 'people');

        await postData({
            film: movieID,
            person: cast.id,
            cast_id: cast.cast_id,
            character: cast.character,
            credit_id: cast.credit_id,
            order: cast.order,
        }, 'film_cast');
    }
    //directors
    for (const director of creditResponse.crew.filter(crewMember => crewMember.job === 'Director')) {
        console.log('Posting director data:', director);
        await postData({
            id: director.id,
            adult: director.adult || false,
            gender: director.gender || 1,
            tmdb_id: director.id || 0,
            known_for_department: 'directing',
            name: director.name || '',
            popularity: director.popularity || 0,
            profile_path: director.profile_path || '',
        }, 'people');

        await postData({
            film: movieID,
            person: director.id,
            credit_id: director.credit_id,
            department: director.department,
            job: director.job,
        }, 'film_crew');
    }
};



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
search_button.addEventListener('click', async () => {
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
// Handle Popular button click
document.querySelectorAll('.popular_button').forEach(button => {
    button.addEventListener('click', async () => {
        const popular_page = button.value.trim();  // Get value from the clicked button

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
        } else {
            alert('Please enter a search term.');
        }
    });
});
//handle post button click
document.querySelectorAll('.post_movies').forEach(button => {
    button.addEventListener('click', async () => {
        const movieID = button.value.trim();  // Get movie ID from the button's data attribute
        console.log('movieID:', movieID);

        try {
            // Get movie details (assuming `postToMountainMovieDB` and `postCreditsToMountainMovieDB` are working functions)
            // const movie = await fetchData(pop_url(movieID));  // Fetch the full movie object using the movieID (or adjust this to your needs)
            // await postToMountainMovieDB(movie);
            // await postCreditsToMountainMovieDB(movieID);
        } catch (error) {
            console.error("Error in posting movie data:", error);
        }
    });
});

resultsDiv.addEventListener('click', async (e) => {
    // Find the closest parent button element if the image is clicked
    const button = e.target.closest('.post_movies');

    if (button) {
        const movieID = button.value.trim();  // Get movie ID from the button's value
        console.log('movieID:', movieID);

        try {
            // Fetch movie details using the movie ID
            const movie_details = await getMovieDetails(movieID);
            console.log('Fetched movie details:', movie_details);
            // const cast_crew = await getMovieCredits(movieID);
            // Post data to MountainMovie DB
            await postToMountainMovieDB(movie_details);
            await postCreditsToMountainMovieDB(movieID);
        } catch (error) {
            console.error("Error in posting movie data:", error);
        }
    }
});