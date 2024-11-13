export const getCsrfToken = () => {
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookieValue ? cookieValue.split('=')[1] : '';
};

export const apiEndpoint = (object) => {
    return `${window.location.origin}/api/${object}/`;
};


const getOptions = {
    method: 'GET',
    headers: {
        accept: 'application/json',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        }
    }
};

export const deleteData = async (id, apiObject) => {
    console.log(`deleteData called for ${id} in ${apiObject}`);
    const apiEndpoint = `${window.location.origin}/api/${apiObject}/${id}/`;  // Assuming the id is part of the URL

    // Log the API endpoint for the DELETE request
    console.log(`Deleting data from ${apiEndpoint}:`, { id });

    try {
        const response = await fetch(apiEndpoint, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            // Log the error response if the request fails
            console.error(`Error response from ${apiEndpoint}:`, errorData);
            throw new Error(`Error: ${response.status} ${response.statusText} - ${JSON.stringify(errorData)}`);
        }

        // Log success message if the data was successfully deleted
        console.log(`Data with ID ${id} successfully deleted.`);
    } catch (error) {
        // Log any other errors that occur
        console.error(`Error deleting data with ID ${id}:`, error);
    }
};



export const getMMData = async (table) => {
    try {
        console.log(`Fetching data from: ${table}`);
        const url = apiEndpoint(table);
        const response = await window.fetch(url, getOptions);  
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data);
        return data;
    } catch (err) {
        console.error('Error fetching data:', err);
    }
}

export const postData = async (object, apiObject) => {
    console.log('postData called with:', object, apiObject);
    const apiEndpoint = `${window.location.origin}/api/${apiObject}/`;

    // Log the API endpoint and the data being sent
    console.log(`Posting data to ${apiEndpoint}:`, object);

    try {
        const response = await fetch(apiEndpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify(object),
        });

        if (!response.ok) {
            const errorData = await response.json();
            // Log the error response if the request fails
            console.error(`Error response from ${apiEndpoint}:`, errorData);
            throw new Error(`Error: ${response.status} ${response.statusText} - ${JSON.stringify(errorData)}`);
        }

        const result = await response.json();
        // Log success message and result
        console.log(`${object} data posted successfully:`, result);
    } catch (error) {
        // Log any other errors that occur
        console.error(`Error posting ${objec}t data:`, error);
    }
};

// Function Post to MountainMovie DB with movie object
export const postMovieToMountainMovieDB = async (movie) => {
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
export const postCreditsToMountainMovieDB = async (creditResponse) => {
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

// function to post seen_movie
export const postSeenMovie = async (user, movieID) => {
    const customID = Number(`${user}${movieID}`);
    await postData({
        id: customID,
        film: movieID,
        seen_film: true,
        viewer: user,
        viewr_rating: .5
    }, 'seen_films');
    console.log('Posted to MountainMovie DB:');
}

// function to post to watchlist
export const postToWatchlist = async (user, movieID) => {
    const customID = Number(`${user}${movieID}`);

    await postData({
        id: customID,
        film: movieID,
        watchlist: true,
        viewer: user
    }, 'watchlist');
    console.log('Posted to MountainMovie DB:');
}

// export const getSeenMoviesByViewer = async (user) => {
//     const data = await fetchData(`http://
//     localhost:8000/api/seen_movies/`);