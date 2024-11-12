document.getElementById("notificationDropdown").addEventListener("mouseenter", fetchNotifications);

function fetchNotifications() {
    fetch("/api/notifications/")
    .then(response => response.json())
    .then(data => {
        const notificationContainer = document.getElementById("notificationsPlaceholder");
        const notificationCount = document.getElementById("notificationCount");

        // Clear placeholder text
        notificationContainer.innerHTML = "";

        const unreadNotifications = data.filter(notification => !notification.is_read);

        if (unreadNotifications.length > 0) {
            notificationCount.textContent = unreadNotifications.length;  // Display unread count
            unreadNotifications.forEach(notification => {
                const notificationItem = document.createElement("a");
                notificationItem.classList.add("dropdown-item");
                notificationItem.href = `/feed_entry/${notification.feed_entry}/`;
                notificationItem.textContent = `${notification.notification_type === "like" ? "👍" : "💬"} ${notification.notification_type} on ${new Date(notification.timestamp).toLocaleString()}`;
                
                // Add event listener to mark notification as read on click
                notificationItem.addEventListener("click", (event) => {
                    event.preventDefault();  // Prevent immediate navigation
                    markNotificationAsRead(notification.id, notificationItem.href);
                });

                notificationContainer.appendChild(notificationItem);
            });
        } else {
            notificationCount.style.display = "none";  // Hide bubble if no notifications
            notificationContainer.innerHTML = `<div class="dropdown-item text-center text-muted">No new notifications</div>`;
        }
    })
    .catch(error => console.error("Error fetching notifications:", error));
}

function markNotificationAsRead(notificationId, redirectUrl) {
    console.log("Marking notification as read:", notificationId);  // Debugging line

    fetch(`/api/notifications/${notificationId}/mark_as_read/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok) {
            console.log("Notification marked as read");  // Confirm successful request
            window.location.href = redirectUrl;  // Navigate to the post after marking as read
        } else {
            console.error("Failed to mark notification as read");
        }
    })
    .catch(error => console.error("Error marking notification as read:", error));
}

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
