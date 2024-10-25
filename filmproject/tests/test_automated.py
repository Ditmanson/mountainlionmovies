import re
from playwright.sync_api import Page, expect
import pytest
from filmproject.models import User
from django.core.management import call_command
from django.contrib.auth.hashers import make_password

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
    page.get_by_role("button", name="Fetch Movies").click()
    card=page.locator("div.card-body").first
    expect(card).to_be_visible()
    
    # check about us page
    page.get_by_role("link", name="Mountain Lion Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="About Us").click()
    ## TODO: Add more tests here when the about us page is updated

def test_user_login(page: Page):
    user = 'travis'
    password = "password1234!@#$"
    hashed_password = make_password(password)
    page.goto("http://localhost:8000")
    page.get_by_role("button", name="Menu").click()
    page.get_by_label("", exact=True).get_by_role("link", name="Login").click()
    page.fill('input[name="username"]', user)
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
    page.get_by_role("link", name=user).click()
    # expect(page).to_have_url(re.compile(r"http://localhost:8000/viewers/.*"))
    # TODO we need to add class names or something so i can get a generic locator
    # expect(page).to_have_text("Scream")
