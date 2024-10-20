import re
from playwright.sync_api import Page, expect
import pytest
from filmproject.models import User

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
    page.locator('.flex-grow-1').first.click() 
    page.get_by_role("link", name="Back to Film List").click()
    page.locator(".d-inline > .btn").first.click()
    expect(page).to_have_url(re.compile(r"http://localhost:8000/login/.*"))
    
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


# class TestLoggedInFeatures:

#     @pytest.fixture
#     def setup_method(self):
#         # Setup code: create a test user
#         user = User.objects.create_user(username='yodaddy', password='123')
#         yield user  # Yield the user object for the tests
#         # Teardown code: delete the user after tests
#         user.delete()

#     def test_user_login(self, page):
#         # Use the setup_method fixture
#         page.goto("http://localhost:8000/login/")
#         page.fill('input[name="username"]', 'yodaddy')
#         page.fill('input[name="password"]', '123')
#         page.wait_for_timeout(1000)
#         page.get_by_role("button", name="Continue").click()
#         page.wait_for_timeout(5000)

