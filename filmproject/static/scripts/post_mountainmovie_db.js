export const getCsrfToken = () => {
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookieValue ? cookieValue.split('=')[1] : '';
};

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
