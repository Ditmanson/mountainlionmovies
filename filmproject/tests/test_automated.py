import re
from playwright.sync_api import Page, expect
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

# If you wan tto see the tests make sure you run pytest --headed
def test_not_logged_in(page: Page):
    # go to localhost, we use this local host because of ci/cd
    page.goto("http://localhost:8000")
    # page.wait_for_timeout(500)
    
    # Check Films not logged in actions
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    expect(page).to_have_url(re.compile(r"http://localhost:8000/films/"))
    # page.wait_for_timeout(500)
    
    #TODO we need to make test data. I think it will be easier to do this after seiralizers are done
    # page.locator('.flex-grow-1').first.click() 
    # page.get_by_role("link", name="Back to Film List").click()
    # page.locator(".d-inline > .btn").first.click()
    # expect(page).to_have_url(re.compile(r"http://localhost:8000/login/.*"))
    
    # check viewers not logged in actions
    page.get_by_role("link", name="Mountain Lion Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Viewers").click()
    expect(page).to_have_url(re.compile(r"http://localhost:8000/viewers/"))
    
    # check search actions
    page.get_by_role("link", name="Mountain Lion Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Search").click()
    page.get_by_placeholder("string").fill("alien")
    page.get_by_placeholder("string").press("Enter")
    alien_card=page.get_by_role("heading", name="Alien", exact=True).first
    expect(alien_card).to_be_visible()
    
    # check search popular movie actions
    page.get_by_role("link", name="Mountain Lion Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Popular").click()
    page.get_by_placeholder("Page number").fill("1")
    page.get_by_placeholder("Page number").press("Enter")
    card=page.locator("div.card-body").first
    expect(card).to_be_visible()
    
    # check about us page
    page.get_by_role("link", name="Mountain Lion Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="About Us").click()
    ## TODO: Add more tests here when the about us page is updated

# # Fixture to set up test data
# @pytest.fixture(scope="module")
# def create_test_user():
#     # Create a user with a hashed password
#     user = User(
#         username="bobby",
#         password=make_password("password1234!@#$"),
#         email="bobby@hotmail.com",
#         is_staff=True,
#         is_active=True,
#         is_superuser=True
#     )
#     user.save()
#     yield  # This allows the test to run while the user is set up
#     user.delete()  # Clean up after the tests

def test_user_login(page: Page):
    user = 'bob'
    password = "password1234!@#$"
    hashed_password = make_password(password)
    page.goto("http://localhost:8000")
    page.get_by_role("button", name="Menu").click()
    page.get_by_label("", exact=True).get_by_role("link", name="Login").click()
    page.fill('input[name="username"]', 'bob')
    page.fill('input[name="password"]', password)
    # page.wait_for_timeout(2000)
    page.get_by_role("button", name="Continue").click()
    # page.wait_for_timeout(2000)
    expect(page).to_have_url(re.compile(r"http://localhost:8000/accounts/profile"))
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    # page.wait_for_timeout(2000)
    page.locator(".d-inline > .btn").first.click()
    page.locator("div:nth-child(2) > .d-flex > .d-inline-flex > form:nth-child(2) > .btn").click()
    # page.wait_for_timeout(2000)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Viewers").click()
    page.get_by_role("link", name="bob").click()
    # expect(page).to_have_url(re.compile(r"http://localhost:8000/viewers/.*"))
    # TODO we need to add class names or something so i can get a generic locator
    # expect(page).to_have_text("Scream")

@pytest.mark.django_db
def test_send_email(client):
    # Send email
    mail.send_mail(
        'Test Email',
        'This is a test email.',
        'from@example.com',
        ['to@example.com'],
    )

    # Check if email was sent
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == 'Test Email'
    assert mail.outbox[0].body == 'This is a test email.'
    assert mail.outbox[0].from_email == 'from@example.com'
    assert mail.outbox[0].to == ['to@example.com']


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
def test_user_registration(page: Page):
    user = "testuser"
    email = "testuser@example.com"
    password = "PasswordTest123#@!"
    hashed_password = make_password(password)
    page.goto("http://localhost:8000/register/")

    page.fill('input[name="username"]', user)
    page.fill('input[name="email"]', email)
    page.fill('input[name="password1"]', password)
    page.fill('input[name="password2"]', password)
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Register").click()
    page.wait_for_timeout(4000)

    # Check if any form error messages are displayed
    form_errors = page.locator(".errorlist").all_text_contents()
    if form_errors:
        print("Form validation errors:", form_errors)
    expect(page).to_have_url(re.compile(r'http://localhost:8000/register/'))

    print(mail.outbox)


    # Django Mail
    assert len(mail.outbox) == 1
    email = mail.outbox[0]
    assert email.subject == "Activate your account."

    activation_link = re.search(r'http://localhost:8000/accounts/activate/(.+)/(.+)/', email.body)
    assert activation_link is not None, "Activation link not found in email."

    # Decode user ID
    uidb64, token = activation_link.groups()

    user_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=user_id)
    assert user.is_active is False

    page.goto(f"http://localhost:8000/accounts/activate/{uidb64}/{token}/")
    expect(page).to_have_url(re.compile(r"http://localhost:8000/accounts/activation_complete/"))
    user.refresh_from_db()
    assert user.is_active is True
