export const getCsrfToken = () => {
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookieValue ? cookieValue.split('=')[1] : '';
};

export const postData = async (movie, apiObject) => {
    console.log('postData called with:', movie, apiObject);
    const apiEndpoint = `${window.location.origin}/api/${apiObject}/`;

    // Log the API endpoint and the data being sent
    console.log(`Posting data to ${apiEndpoint}:`, movie);

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
            // Log the error response if the request fails
            console.error(`Error response from ${apiEndpoint}:`, errorData);
            throw new Error(`Error: ${response.status} ${response.statusText} - ${JSON.stringify(errorData)}`);
        }

        const result = await response.json();
        // Log success message and result
        console.log('Movie data posted successfully:', result);
    } catch (error) {
        // Log any other errors that occur
        console.error('Error posting movie data:', error);
    }
};
