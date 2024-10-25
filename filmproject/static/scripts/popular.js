import './fetch_tmdb_data.js';
import './post_mountainmovie_db.js';
import { credits_url, pop_url, image_url, fetchData } from './fetch_tmdb_data.js';
import { postData, getCsrfToken } from './post_mountainmovie_db.js';

document.addEventListener('DOMContentLoaded', () => {
    const display_results = async (data) => {
        const results_div = document.getElementById('results');
        results_div.innerHTML = ''; // Clear previous results

        if (data.results) {
            for (const movie of data.results) {
                const movie_element = document.createElement('div');
                movie_element.classList.add('card', 'mb-2');
                movie_element.innerHTML = `
                    <div class="card-body">
                        <h5 class="card-title">${movie.title}</h5>
                        <p class="card-text">Rating: ${movie.vote_average}</p>
                        <p class="card-text">${movie.overview}</p>
                        <p class="card-text">${movie.id}</p>
                        <img src="${image_url}${movie.poster_path}" class="img-fluid" alt="${movie.title}">
                    </div>`;
                results_div.appendChild(movie_element);

                if (shouldPost) {
                    console.log('trying to post', shouldPost);
                    const creditResponse = await fetchData(credits_url(movie.id));
                    console.log('creditResponse:', creditResponse);
                    if (creditResponse) {
                        // console.log('creditResponse.ok:', creditResponse.ok);
                        // const credits = await creditResponse.json();
                        // console.log('credits:', credits);
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
                        }

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
                        }

                        await postData({
                            id: movie.id,
                            adult: movie.adult,
                            backdrop_path: movie.backdrop_path,
                            belongs_to_collection: movie.belongs_to_collection,
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
                    }
                }
            }
        } else {
            results_div.innerHTML = '<p>No results found</p>';
        }
    };

    let shouldPost = document.getElementById('postCheckbox').checked;
    console.log('Initial shouldPost:', shouldPost);

    document.getElementById('fetchButton').addEventListener('click', async () => {
        const pageInput = document.getElementById('pageInput').value;
        if (pageInput) {
            const data = await fetchData(pop_url(pageInput));
            display_results(data);
        } else {
            alert('Please enter a page number.');
        }
    });

    document.getElementById('postCheckbox').addEventListener('change', () => {
        shouldPost = document.getElementById('postCheckbox').checked;
        console.log('Changed shouldPost:', shouldPost);
    });

    document.getElementById('pageInput').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            document.getElementById('fetchButton').click();
        }
    });
});
