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
      console.log(data);
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
        </div>
      `;
      resultsDiv.appendChild(movieElement);
    });
  } else {
    resultsDiv.innerHTML = '<p>No movies found.</p>';
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

/**
 * Same as up there except we are also going to accept pressing enter
 */
document.getElementById('pageInput').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    document.getElementById('fetchButton').click();
  }
});