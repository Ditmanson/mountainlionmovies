/**
 * this part is copy and paste from the API documentation
 * We should change this authorization to take it from .env file
 * That's not crucial though, this api is free and we get 40 requests a second.
 * I don't really care if it's compromised. I'll make a new key for myself later.
 */
const options = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyODY2NjUyMi4xNDkxNjMsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._nORPBk_Vz0YNM_Rav4nMW5_x2d92IbmXaXjNy_ObEc'
  }
};
/**
 * This part is also copy and paste from the api documentation
 * The only thing I changed is I took the results and sent it to a function to render html
 * And then I added a console log of the data
 * The .catch is just a console log for error handling. it's not necessary but it's like best practice or whatever
 * 
 */
const fetchMovies = (page) => {
  fetch(`https://api.themoviedb.org/3/movie/popular?language=en-US&page=${page}`, options)
    .then((response) => response.json())
    .then((data) => {
      displayResults(data);
    })
    .catch((err) => console.error(err));
};
/**
 * So if you pull up the console log here you'll see what's going on
 * data is everything returned from the API
 * inside the data object there's an array called results
 * so data.results.forEach is going to loop through that array
 * Then we assign each of those attributes to a new object called movie
 * so you'll see you can pull  up some other information with that
*/
const displayResults = (data) => {
  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = ''; // Clear previous results
  const baseUrl = 'https://image.tmdb.org/t/p/w500'; // Base URL for images

  if (data.results) {
    data.results.forEach(movie => {
      const movieElement = document.createElement('div');
      movieElement.classList.add('card', 'mb-2');
      movieElement.innerHTML = `
      <div class="card-body">
      <h5 class="card-title">${movie.title}</h5>
      <p class="card-text">Rating: ${movie.vote_average}</p>
      <p class="card-text">${movie.overview}</p>
      <img src="${baseUrl}${movie.poster_path}" class="img-fluid" alt="${movie.title}">
      </div>`;
      resultsDiv.appendChild(movieElement);
    });
    // TODO get some logic to decide if your a super user
    // const apiButton = document.createElement('button');
    // apiButton.classList.add('btn', 'btn-primary', 'mb-2');
    // apiButton.innerHTML = 'Post All Movie Data';
    // apiButton.addEventListener('click', () => {
    if (isSuperuser) {
      data.results.forEach(movie => {
        postMovieData({
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
        });
      });
    }

    // });

    // Append the button to the results div
    // resultsDiv.appendChild(apiButton);
  } else {
    resultsDiv.innerHTML = '<p>No movies found.</p>';
  }
};


// reference so for travis please don't delete
// function post1() {
//   curl -X POST https://app-tditmans-5.devedu.io/api/films/ \
//   -H "Content-Type: application/json" \
//   -d @mock_data3.json
//   }
// post movie data to  sqlite database
const getCsrfToken = () => {
  const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
  return cookieValue ? cookieValue.split('=')[1] : '';
};

const postMovieData = async (movie) => {
  const apiEndpoint = `${window.location.origin}/api/films/`;

  try {
    const response = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken(), // Add CSRF token here
      },
      body: JSON.stringify(movie),
    });

    if (!response.ok) {
      const errorData = await response.json(); // Capture error details
      throw new Error(`Error: ${response.status} ${response.statusText} - ${JSON.stringify(errorData)}`);
    }

    const result = await response.json();
    console.log('Movie data posted successfully:', result);
  } catch (error) {
    console.error('Error posting movie data:', error);
  }
};



/**
 * So here because we are using vanilla javascript we create the event listener and attach it to an id
 */
document.getElementById('fetchButton').addEventListener('click', () => {
  const pageInput = document.getElementById('pageInput').value;
  if (pageInput) {
    fetchMovies(pageInput);
  } else {
    alert('Please enter a page number.');
  }
});
let isSuperuser = document.getElementById('postCheckbox').value;
/**
 * So here because we are using vanilla javascript we create the event listener and attach it to an id
 */
document.getElementById('postCheckbox').addEventListener('click', () => {
  isSuperuser = document.getElementById('postCheckbox').value;
});

/**
 * Same as up there except we are also going to accept pressing enter
 */
document.getElementById('pageInput').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    document.getElementById('fetchButton').click();
  }
});
