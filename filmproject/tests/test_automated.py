import re
from playwright.sync_api import Page, expect, sync_playwright
from asgiref.sync import sync_to_async
import pytest
from filmproject.models import User
from django.core.management import call_command
from django.contrib.auth.hashers import make_password

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.core import mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from filmproject.tokens import account_activation_token
from django.test import Client

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.core import mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from filmproject.tokens import account_activation_token
from django.test import Client

def test_automated_from_playwright(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Popular").click()
    page.get_by_label("Post All Movie Data").check()
    page.get_by_placeholder("Page number").click()
    page.get_by_placeholder("Page number").fill("1")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > .d-flex > .d-inline-flex > form > .btn").first.click()
    page.locator("div:nth-child(3) > .d-flex > .d-inline-flex > form > .btn").first.click()
    page.locator("div:nth-child(4) > .d-flex > .d-inline-flex > form > .btn").first.click()
    page.locator("div:nth-child(4) > .d-flex > .d-inline-flex > form:nth-child(2) > .btn").click()
    page.locator("div:nth-child(3) > .d-flex > .d-inline-flex > form:nth-child(2) > .btn").click()
    page.locator("div:nth-child(2) > .d-flex > .d-inline-flex > form:nth-child(2) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()
   

# If you wan tto see the tests make sure you run pytest --headed
# def test_not_logged_in(page: Page):
#     # go to localhost, we use this local host because of ci/cd
#     page.goto("http://localhost:8000")
#     # page.wait_for_timeout(500)
    
#     # Check Films not logged in actions
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Films").click()
#     expect(page).to_have_url(re.compile(r"http://localhost:8000/films/"))
#     # page.wait_for_timeout(500)
    
#     #TODO we need to make test data. I think it will be easier to do this after seiralizers are done
#     # page.locator('.flex-grow-1').first.click() 
#     # page.get_by_role("link", name="Back to Film List").click()
#     # page.locator(".d-inline > .btn").first.click()
#     # expect(page).to_have_url(re.compile(r"http://localhost:8000/login/.*"))
    
#     # check viewers not logged in actions
#     page.get_by_role("link", name="Mountain Lion Movies").click()
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Viewers").click()
#     expect(page).to_have_url(re.compile(r"http://localhost:8000/viewers/"))
    
#     # check search actions
#     page.get_by_role("link", name="Mountain Lion Movies").click()
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Search").click()
#     page.get_by_placeholder("string").fill("alien")
#     page.get_by_placeholder("string").press("Enter")
#     alien_card=page.get_by_role("heading", name="Alien", exact=True).first
#     expect(alien_card).to_be_visible()
    
#     # check search popular movie actions
#     page.get_by_role("link", name="Mountain Lion Movies").click()
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Popular").click()
#     page.get_by_placeholder("Page number").fill("1")
#     page.get_by_role("button", name="Fetch Movies").click()
#     card=page.locator("div.card-body").first
#     expect(card).to_be_visible()
    
#     # check about us page
#     page.get_by_role("link", name="Mountain Lion Movies").click()
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="About Us").click()
#     ## TODO: Add more tests here when the about us page is updated

# def test_user_login(page: Page):
#     user = 'travis'
#     password = "password1234!@#$"
#     hashed_password = make_password(password)
#     page.goto("http://localhost:8000")
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_label("", exact=True).get_by_role("link", name="Login").click()
#     page.fill('input[name="username"]', user)
#     page.fill('input[name="password"]', password)
#     # page.wait_for_timeout(2000)
#     page.get_by_role("button", name="Continue").click()
#     # page.wait_for_timeout(2000)
#     expect(page).to_have_url(re.compile(r"http://localhost:8000/accounts/profile"))
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Films").click()
#     # page.wait_for_timeout(2000)
#     page.locator(".d-inline > .btn").first.click()
#     page.locator("div:nth-child(2) > .d-flex > .d-inline-flex > form:nth-child(2) > .btn").click()
#     # page.wait_for_timeout(2000)
#     page.get_by_role("button", name="Menu").click()
#     page.get_by_role("link", name="Viewers").click()
#     page.get_by_role("link", name=user).click()
#     # expect(page).to_have_url(re.compile(r"http://localhost:8000/viewers/.*"))
#     # TODO we need to add class names or something so i can get a generic locator
#     # expect(page).to_have_text("Scream")

@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    EMAIL_USE_TLS=False,
    EMAIL_HOST='localhost',
    EMAIL_PORT=1025,
)
def test_user_registration(live_server, transactional_db):
    user = "testuser"
    email = "testuser@example.com"
    password = "PasswordTest123#@!"

    # Simulate file upload
    with open('filmproject/media/profile_pictures/dummyPFP.jpg', 'rb') as img:
        profile_pic = SimpleUploadedFile(
            name='dummyPFP.jpg',
            content=img.read(),
            content_type='image/jpeg'
        )

    mail.outbox = []  # Clear any existing emails

    # Now use Playwright to automate the browser interaction
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the registration page
        #page.goto(f"{live_server.url}/register/")
        page.goto(live_server.url)
        page.get_by_role("link", name="Login").click()
        page.get_by_role("link", name="Sign Up").click()

        # Fill the registration form
        page.fill('input[name="username"]', user)
        page.fill('input[name="email"]', email)
        page.fill('input[name="password1"]', password)
        page.fill('input[name="password2"]', password)
        with page.expect_file_chooser() as fc_info:
            page.click('input[name="profile_picture"]')
        file_chooser = fc_info.value
        file_chooser.set_files("filmproject/media/profile_pictures/dummyPFP.jpg")
        page.get_by_role("button", name="Continue").click()

        # Wait for the page to load and network requests to finish
        page.wait_for_load_state("networkidle")

        # Ensure the email was sent
        assert len(mail.outbox) == 1, "No email was sent"
        activation_email = mail.outbox[0]
        assert activation_email.subject == "Activate your account."

        # Navigate to the activation link (retrieved from the email)
        print(f"Email body: {activation_email.body}")
        server_url = re.escape(live_server.url)
        activation_link = re.search(rf'{server_url}/activate/([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)/', activation_email.body)
        assert activation_link is not None, "Activation link not found in email."

        uidb64, token = activation_link.groups()

        # Simulate activation through the browser
        page.goto(f"{live_server.url}/activate/{uidb64}/{token}/")
        page.wait_for_timeout(2000)

        # Close the browser
        context.close()
        browser.close()

        # Decode the user ID
    user_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=user_id)
    
    # Assert that the user is now active
    assert user.is_active is True
