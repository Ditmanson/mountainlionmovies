// Function to get CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Function to handle "Like" functionality
window.likeEntry = function (entryId) {
    fetch(`/like_entry/${entryId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token to headers
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById(`like-count-${entryId}`).innerText = `${data.likes} Likes`;
        }
    })
    .catch(error => console.error("Error liking entry:", error));
}

// Function to handle "Comment" functionality
window.commentEntry = function (entryId) {
    const input = document.getElementById("comment-content");
    const content = input.value.trim();
    
    if (!content) return;  // If empty, do nothing

    fetch(`/comment_entry/${entryId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token to headers
        },
        body: JSON.stringify({ content })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let commentsDiv = document.getElementById(`comments-${entryId}`);
            let newComment = document.createElement('li');
            newComment.classList.add("list-group-item");
            newComment.innerHTML = `<strong>${data.user}:</strong> ${data.content}`;
            commentsDiv.appendChild(newComment);
            input.value = '';  // Clear the input box
        }
    })
    .catch(error => console.error("Error commenting on entry:", error));
}
