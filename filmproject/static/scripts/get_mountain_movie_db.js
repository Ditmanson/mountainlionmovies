export const getCsrfToken = () => {
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookieValue ? cookieValue.split('=')[1] : '';
};

// const apiEndpoint = `${window.location.origin}/api/${object}/`;
export const apiEndpoint = (object) => {
    return `${window.location.origin}/api/${object}/`;
};

const options = {
    method: 'GET',
    headers: {
        accept: 'application/json',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        }
    }
};

export const getData = async (url) => {
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
}