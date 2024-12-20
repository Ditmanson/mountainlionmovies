import { fetchData } from './tmdb_data.js';
// static/scripts/social_feed.js

console.log("Script loaded successfully.");

const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWEzNmRhMWI5ZmU4ZTEzMmQxZWNhM2MwZDcwYTI4YyIsIm5iZiI6MTcyODY2NjUyMi4xNDkxNjMsInN1YiI6IjY3MDU5ODE3ZjRiOTE5ZjgzOTc3OGI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._nORPBk_Vz0YNM_Rav4nMW5_x2d92IbmXaXjNy_ObEc'
    }
};
console.log("Options set:", options);

// Debounce function to limit the rate at which fetchFeed is called
function debounce(func, delay) {
    console.log("Initializing debounce function with delay:", delay);
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

let currentPage = 1; // Track the current page of posts
console.log("Initial page set to:", currentPage);

// Modify fetchFeed to accept a page parameter
async function fetchFeed(page = 1) {
    console.log(`Fetching feed for page ${page}...`);
    try {
        const response = await fetch(`/feed_entries/?page=${page}`);
        const feedEntries = await response.json();
        console.log("Fetched feed entries:", feedEntries);

        const feedContainer = document.getElementById('feed-container');
        if (!feedContainer) {
            console.error("Feed container not found in the DOM.");
            return;
        }

        // Only clear previous entries if it's the first page
        if (page === 1) {
            console.log("Clearing previous entries for initial load.");
            feedContainer.innerHTML = ''; // Clear previous entries on initial load
        }

        // Process each entry
        for (const entry of feedEntries) {
            console.log("Processing entry:", entry);
            const tmdbUrl = `https://api.themoviedb.org/3/movie/${entry.movie.tmdb_id}`;
            const tmdbData = await fetchData(tmdbUrl, options);
            console.log("Fetched TMDb data:", tmdbData);

            // Render feed item with TMDb details
            const feedItem = document.createElement('div');
            feedItem.className = 'feed-item card mb-3';
            feedItem.innerHTML = `
              <div class="card-body d-flex align-items-center">
                <img src="${tmdbData.poster_path ? 'https://image.tmdb.org/t/p/w500' + tmdbData.poster_path : '{% static "images/default_movie_poster.jpg" %}'}" class="rounded img-thumbnail mr-3" alt="${tmdbData.title}" style="width: 100px; height: auto;">
                <div>
                  <h5 class="card-title mb-1">${entry.user}</h5>
                  <p class="card-text">${entry.user} ${entry.action} <strong>${tmdbData.title}</strong></p>
                  <small class="text-muted">${entry.timestamp}</small>
                  <p class="mt-2">${tmdbData.overview}</p>
                  <div class="mt-2">
                    <button class="btn btn-sm btn-primary" onclick="likeEntry(${entry.id})">Like</button>
                    <span id="like-count-${entry.id}">${entry.likes} Likes</span>
                  </div>
                  <div class="mt-2">
                    <input type="text" class="form-control form-control-sm" placeholder="Add a comment..." onkeypress="if(event.key === 'Enter') commentEntry(${entry.id}, this)">
                  </div>
                  <div id="comments-${entry.id}" class="mt-2">
                    ${entry.comments.map(comment => `<p><strong>${comment.user}:</strong> ${comment.content}</p>`).join('')}
                  </div>
                </div>
              </div>
            `;
            feedContainer.appendChild(feedItem);
            console.log("Feed item added to container.");
        }

        // Increment currentPage for the next batch
        currentPage += 1;
        console.log("Page incremented to:", currentPage);
    } catch (error) {
        console.error("Error fetching feed:", error);
    }
}

// Check if the user has scrolled to the bottom of the feed container
function checkScrollAndLoadMore() {
    const feedContainer = document.getElementById('feed-container');
    if (!feedContainer) {
        console.error("Feed container not found in the DOM.");
        return;
    }
    const feedContainerBottom = feedContainer.getBoundingClientRect().bottom;
    const windowBottom = window.innerHeight;

    // If the bottom of the feed container is within the visible window, load more
    if (feedContainerBottom <= windowBottom) {
        console.log("Reached bottom of feed. Loading more posts...");
        fetchFeed(currentPage);
    }
}

// Attach the scroll event listener to window with a debounce function
window.addEventListener('scroll', debounce(checkScrollAndLoadMore, 300));
console.log("Scroll event listener attached.");


// Function to get CSRF token from the cookie
function getCookie(name) {
    console.log("Getting CSRF token from cookies...");
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
    console.log("CSRF token retrieved:", cookieValue);
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Function to handle "Like" functionality
window.likeEntry = function (entryId) {
    console.log(`Liking entry ${entryId}...`);
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
            console.log(`Entry ${entryId} liked successfully. Updated like count: ${data.likes}`);
        }
    })
    .catch(error => console.error("Error liking entry:", error));
}

// Function to handle "Comment" functionality
window.commentEntry = function (entryId, input) {
    console.log(`Commenting on entry ${entryId} with content:`, input.value);
    fetch(`/comment_entry/${entryId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token to headers
        },
        body: JSON.stringify({ content: input.value })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let commentsDiv = document.getElementById(`comments-${entryId}`);
            let newComment = document.createElement('p');
            newComment.innerHTML = `<strong>${data.user}:</strong> ${data.content}`;
            commentsDiv.appendChild(newComment);
            input.value = '';  // Clear the input box
            console.log(`Comment added to entry ${entryId}:`, data.content);
        }
    })
    .catch(error => console.error("Error commenting on entry:", error));
}

// Initial load of the first page
fetchFeed(currentPage);
console.log("Initial feed fetch called.");

document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM fully loaded and parsed.");
    const feedContainer = document.getElementById('feed-container');

    // If feedContainer is null, log an error
    if (!feedContainer) {
        console.error("Feed container not found in the DOM.");
        return;
    }

    // Debounced function to fetch feed only when user scrolls to the top
    const debouncedFetchFeed = debounce(() => {
        console.log("Scroll event detected in feed container.");

        if (feedContainer.scrollTop === 0) {
            console.log("User scrolled to the top. Refreshing feed...");
            fetchFeed();
        }
    }, 300);

    // Attach the scroll event listener to the feed container
    feedContainer.addEventListener('scroll', debouncedFetchFeed);
    console.log("Scroll event listener attached to feed container.");
});
