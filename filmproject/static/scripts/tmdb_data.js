export const credits_url = (movieID) => {
  return `https://api.themoviedb.org/3/movie/${movieID}/credits?language=en-US`;
};
export const pop_url = (page) => {
  return `https://api.themoviedb.org/3/movie/popular?language=en-US&page=${page}`;
};
export const watch_providers_url = (movieID) => {
  return `https://api.themoviedb.org/3/movie/${movieID}/watch/providers?language=en-US`;
};
export const search_url = (query) => {
  return `https://api.themoviedb.org/3/search/movie?query=${query}`;
};
export const movie_details_url = (movieID) => {
  return `https://api.themoviedb.org/3/movie/${movieID}?language=en-US`;
};
export const image_url = 'https://image.tmdb.org/t/p/w500';

export const getCsrfToken = () => {
  const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
  return cookieValue ? cookieValue.split('=')[1] : '';
};

const options = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyODY2NjUyMi4xNDkxNjMsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._nORPBk_Vz0YNM_Rav4nMW5_x2d92IbmXaXjNy_ObEc'
  }
};
export const fetchData = async (url) => {
  try {
    console.log(`Fetching data from: ${url}`);
    const response = await window.fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('Fetched data:', data);
    return data;
  } catch (err) {
    console.error('Error fetching data:', err);
  }
};


// Function to fetch popular movies
export const popular_movies = async (number = '1') => {
  const data = await fetchData(pop_url(number));
  console.log('Fetched popular movies:', data.results);
  return data.results;
};

// Function to fetch searched movies
export const searched_movies = async (query) => {
  const data = await fetchData(search_url(query));
  console.log('Fetched searched movies:', data.results);
  return data.results;
};

// Function to get Movie Details
export const getMovieDetails = async (movieID) => {
  const data = await fetchData(movie_details_url(movieID));
  console.log('Fetched movie details:', data);
  return data;
};

// Function to get cast and crew
export const getMovieCredits = async (movieID) => {
  const data = await fetchData(credits_url(movieID));
  console.log('Fetched movie credits:', data);
  return data;
};