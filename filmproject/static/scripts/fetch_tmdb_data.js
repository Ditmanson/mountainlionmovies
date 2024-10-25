export const credits_url = (movieID) => {
  return `https://api.themoviedb.org/3/movie/${movieID}/credits?language=en-US`;
};
export const pop_url = (page) => {
  return `https://api.themoviedb.org/3/movie/popular?language=en-US&page=${page}`;
};
export const image_url = 'https://image.tmdb.org/t/p/w500';

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

