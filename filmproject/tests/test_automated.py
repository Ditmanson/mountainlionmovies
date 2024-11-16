import re
from playwright.sync_api import Page, sync_playwright
from django.core import mail
from django.test import override_settings
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from filmproject.models import User


def test_automated_from_playwright(page: Page):
#     # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("button", name="Notifications").click()
    page.get_by_role("button", name="Menu").first.click()
    page.get_by_role("link", name="Browse").click()
    page.get_by_placeholder("string").click()
    page.get_by_placeholder("string").fill("alien")
    page.locator("#search_button").click()
    page.get_by_role("button", name="1").click()



# def test_update_profile(page: Page):
#     page.goto("http://localhost:8000/")
#     page.get_by_role("link", name="Login").click()
#     page.get_by_placeholder("Enter your username").fill("travis")
#     page.get_by_placeholder("Enter your password").fill("password1234!@#$")
#     page.get_by_role("button", name="Continue").click()
#     page.get_by_role("link", name="Update Profile").click()
#     page.get_by_label("Profile picture:").set_input_files(
#         "filmproject/media/profile_pictures/dummyPFP.jpg"
#     )
#     page.get_by_role("button", name="Update").click()
#     page.wait_for_timeout(2000)


# @override_settings(
#     EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
#     EMAIL_USE_TLS=False,
#     EMAIL_HOST="localhost",
#     EMAIL_PORT=1025,
# )
# def test_user_registration(live_server, transactional_db):
#     user = "testuser"
#     email = "testuser@example.com"
#     password = "PasswordTest123#@!"

#     mail.outbox = []  # Clear any existing emails

#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         page = context.new_page()

#         # Navigate to the registration page
#         page.goto(live_server.url)
#         page.get_by_role("link", name="Login").click()
#         page.get_by_role("link", name="Sign Up").click()

#         # Fill the registration form
#         page.fill('input[name="username"]', user)
#         page.fill('input[name="email"]', email)
#         page.fill('input[name="password1"]', password)
#         page.fill('input[name="password2"]', password)
#         page.get_by_role("button", name="Continue").click()

#         # Wait for the page to load and network requests to finish
#         page.wait_for_load_state("networkidle")

#         # Ensure the email was sent
#         assert len(mail.outbox) == 1, "No email was sent"
#         activation_email = mail.outbox[0]
#         assert activation_email.subject == "Activate your account."

#         # Retrieve activation link from the email
#         server_url = re.escape(live_server.url)
#         activation_link = re.search(
#             rf"{server_url}/activate/([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)/",
#             activation_email.body,
#         )
#         assert (
#             activation_link is not None
#         ), "Activation link not found in email."

#         uidb64, token = activation_link.groups()

#         # Simulate activation through the browser
#         page.goto(f"{live_server.url}/activate/{uidb64}/{token}/")
#         page.wait_for_timeout(2000)

#         # Close the browser
#         context.close()
#         browser.close()

#     # Decode the user ID
#     user_id = force_str(urlsafe_base64_decode(uidb64))
#     user = User.objects.get(pk=user_id)

#     # Assert that the user is now active
#     assert user.is_active is True
