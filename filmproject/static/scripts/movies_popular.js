// /**
//  * this part is copy and paste from the API documentation
//  * We should change this authorization to take it from .env file
//  * That's not crucial though, this api is free and we get 40 requests a second.
//  * I don't really care if it's compromised. I'll make a new key for myself later.
//  */

const options = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyODY2NjUyMi4xNDkxNjMsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._nORPBk_Vz0YNM_Rav4nMW5_x2d92IbmXaXjNy_ObEc'
  }
};

// /**
//  * This part is also copy and paste from the api documentation
//  * The only thing I changed is I took the results and sent it to a function to render html
// //  * And then I added a console log of the data
// //  * The .catch is just a console log for error handling. it's not necessary but it's like best practice or whatever
//  * 
// */
const fetchMovies = (page) => {
  // resultsDiv.innerHTML = '';
  fetch(`https://api.themoviedb.org/3/movie/popular?language=en-US&page=${page}`, options)
    .then((response) => response.json())
    .then((data) => {
      displayResults(data);
    })
    .catch((err) => console.error('Error fetching movies:', err)); // Added error handling
};
const fetchCredits = async (movieID) => {
  try {
    const response = await fetch(`https://api.themoviedb.org/3/movie/${movieID}/credits?language=en-US`, options);
    const data = await response.json();
    return data;
  } catch (err) {
    console.error('Error fetching credits:', err);
  }
};


/**
 * So if you pull up the console log here you'll see what's going on
 * data is everything returned from the API
 * inside the data object there's an array called results
 * so data.results.forEach is going to loop through that array
 * Then we assign each of those attributes to a new object called movie
 * so you'll see you can pull  up some other information with that
*/
const baseUrl = 'https://image.tmdb.org/t/p/w500'; // Base URL for images
const displayResults = async (data) => {
  // console.log('is super' + isSuperuser)
  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = ''; // Clear previous results

  if (data.results) {
    for (const movie of data.results) {
      // data.results.forEach(movie => {
      // console.log(movie.id);
      const movieElement = document.createElement('div');
      movieElement.classList.add('card', 'mb-2');
      movieElement.innerHTML = `
        <div class="card-body">
        <h5 class="card-title">${movie.title}</h5>
        <p class="card-text">Rating: ${movie.vote_average}</p>
        <p class="card-text">${movie.overview}</p>
        p class="card-text">${movie.id}</p>
        <img src="${baseUrl}${movie.poster_path}" class="img-fluid" alt="${movie.title}">
        </div>`;
      resultsDiv.appendChild(movieElement);

      if (isSuperuser) {
        const creditResponse = await fetchCredits(movie.id);
        if (creditResponse) {
          for (const director of creditResponse.crew.filter(crewMember => crewMember.job === 'Director')) {
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
        }

        for (const cast of creditResponse.cast) {
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

          // await postData({
          //   film: movie.id,
          //   person: cast.id,
          //   cast_id: cast.cast_id,
          //   character: cast.character || '',
          //   credit_id: cast.credit_id || '',
          //   order: cast.order || 0,
          // }, 'film_cast');
        }

        postData({
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
  } else {
    resultsDiv.innerHTML = '<p>No movies found.</p>';
  }
};
const getCsrfToken = () => {
  const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
  return cookieValue ? cookieValue.split('=')[1] : '';
};

const postData = async (movie, apiObject) => {
  const apiEndpoint = `${window.location.origin}/api/${apiObject}/`;

  try {
    const response = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken(),
      },
      body: JSON.stringify(movie),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(`Error: ${response.status} ${response.statusText} - ${JSON.stringify(errorData)}`);
    }

    const result = await response.json();
    console.log('Movie data posted successfully:', result);
  } catch (error) {
    console.error('Error posting movie data:', error);
  }
};

document.getElementById('fetchButton').addEventListener('click', () => {
  const pageInput = document.getElementById('pageInput').value;
  if (pageInput) {
    fetchMovies(pageInput);
  } else {
    alert('Please enter a page number.');
  }
});

let isSuperuser = document.getElementById('postCheckbox').checked; // Use .checked instead of .value

document.getElementById('postCheckbox').addEventListener('change', () => {
  isSuperuser = document.getElementById('postCheckbox').checked; // Update isSuperuser state
});

document.getElementById('pageInput').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    document.getElementById('fetchButton').click();
  }
});
