
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


import re
from playwright.sync_api import Page, sync_playwright
from django.core import mail
from django.test import override_settings
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from filmproject.models import User


def x_test_automated_from_playwright__mutmut_orig(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_1(page: Page):
    # Create a user
    page.goto("XXhttp://localhost:8000/XX")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_2(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("XXlinkXX", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_3(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="XXLoginXX").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_4(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link",).click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_5(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("XXEnter your usernameXX").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_6(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("XXtravisXX")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_7(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("XXEnter your usernameXX").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_8(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("XXTabXX")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_9(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("XXEnter your passwordXX").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_10(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("XXpassword1234!@#$XX")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_11(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("XXEnter your passwordXX").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_12(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("XXEnterXX")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_13(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("XXbuttonXX", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_14(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="XXMenuXX").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_15(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button",).click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_16(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("XXbuttonXX", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_17(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="XXFetch MoviesXX").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_18(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button",).click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_19(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("XXPage numberXX").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_20(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("XX2XX")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_21(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("XXbuttonXX", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_22(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="XXFetch MoviesXX").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_23(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button",).click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_24(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("XXbuttonXX", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_25(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="XXMenuXX").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_26(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button",).click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_27(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("XXlinkXX", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_28(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="XXFilmsXX").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_29(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link",).click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_30(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("XXdiv:nth-child(2) > form > .btnXX").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_31(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("XXdiv:nth-child(2) > form:nth-child(4) > .btnXX").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_32(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(501)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_33(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("XXbuttonXX", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_34(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="XXMenuXX").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_35(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button",).click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_36(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("XXlinkXX", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_37(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="XXRate MoviesXX").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_38(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link",).click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_39(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("XXbuttonXX", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_40(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="XXCan't DecideXX").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_41(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button",).click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_42(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(501)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_43(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("XXbuttonXX", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_44(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="XXMenuXX").click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_45(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button",).click()
    page.get_by_role("list").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_46(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("XXlistXX").get_by_role("link", name="Profile").click()


def x_test_automated_from_playwright__mutmut_47(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("XXlinkXX", name="Profile").click()


def x_test_automated_from_playwright__mutmut_48(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link", name="XXProfileXX").click()


def x_test_automated_from_playwright__mutmut_49(page: Page):
    # Create a user
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your username").press("Tab")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_placeholder("Page number").fill("2")
    page.get_by_role("button", name="Fetch Movies").click()
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Films").click()
    page.locator("div:nth-child(2) > form > .btn").first.click()
    page.locator("div:nth-child(2) > form:nth-child(4) > .btn").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("link", name="Rate Movies").click()
    page.get_by_role("button", name="Can't Decide").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("list").get_by_role("link",).click()

x_test_automated_from_playwright__mutmut_mutants = {
'x_test_automated_from_playwright__mutmut_1': x_test_automated_from_playwright__mutmut_1, 
    'x_test_automated_from_playwright__mutmut_2': x_test_automated_from_playwright__mutmut_2, 
    'x_test_automated_from_playwright__mutmut_3': x_test_automated_from_playwright__mutmut_3, 
    'x_test_automated_from_playwright__mutmut_4': x_test_automated_from_playwright__mutmut_4, 
    'x_test_automated_from_playwright__mutmut_5': x_test_automated_from_playwright__mutmut_5, 
    'x_test_automated_from_playwright__mutmut_6': x_test_automated_from_playwright__mutmut_6, 
    'x_test_automated_from_playwright__mutmut_7': x_test_automated_from_playwright__mutmut_7, 
    'x_test_automated_from_playwright__mutmut_8': x_test_automated_from_playwright__mutmut_8, 
    'x_test_automated_from_playwright__mutmut_9': x_test_automated_from_playwright__mutmut_9, 
    'x_test_automated_from_playwright__mutmut_10': x_test_automated_from_playwright__mutmut_10, 
    'x_test_automated_from_playwright__mutmut_11': x_test_automated_from_playwright__mutmut_11, 
    'x_test_automated_from_playwright__mutmut_12': x_test_automated_from_playwright__mutmut_12, 
    'x_test_automated_from_playwright__mutmut_13': x_test_automated_from_playwright__mutmut_13, 
    'x_test_automated_from_playwright__mutmut_14': x_test_automated_from_playwright__mutmut_14, 
    'x_test_automated_from_playwright__mutmut_15': x_test_automated_from_playwright__mutmut_15, 
    'x_test_automated_from_playwright__mutmut_16': x_test_automated_from_playwright__mutmut_16, 
    'x_test_automated_from_playwright__mutmut_17': x_test_automated_from_playwright__mutmut_17, 
    'x_test_automated_from_playwright__mutmut_18': x_test_automated_from_playwright__mutmut_18, 
    'x_test_automated_from_playwright__mutmut_19': x_test_automated_from_playwright__mutmut_19, 
    'x_test_automated_from_playwright__mutmut_20': x_test_automated_from_playwright__mutmut_20, 
    'x_test_automated_from_playwright__mutmut_21': x_test_automated_from_playwright__mutmut_21, 
    'x_test_automated_from_playwright__mutmut_22': x_test_automated_from_playwright__mutmut_22, 
    'x_test_automated_from_playwright__mutmut_23': x_test_automated_from_playwright__mutmut_23, 
    'x_test_automated_from_playwright__mutmut_24': x_test_automated_from_playwright__mutmut_24, 
    'x_test_automated_from_playwright__mutmut_25': x_test_automated_from_playwright__mutmut_25, 
    'x_test_automated_from_playwright__mutmut_26': x_test_automated_from_playwright__mutmut_26, 
    'x_test_automated_from_playwright__mutmut_27': x_test_automated_from_playwright__mutmut_27, 
    'x_test_automated_from_playwright__mutmut_28': x_test_automated_from_playwright__mutmut_28, 
    'x_test_automated_from_playwright__mutmut_29': x_test_automated_from_playwright__mutmut_29, 
    'x_test_automated_from_playwright__mutmut_30': x_test_automated_from_playwright__mutmut_30, 
    'x_test_automated_from_playwright__mutmut_31': x_test_automated_from_playwright__mutmut_31, 
    'x_test_automated_from_playwright__mutmut_32': x_test_automated_from_playwright__mutmut_32, 
    'x_test_automated_from_playwright__mutmut_33': x_test_automated_from_playwright__mutmut_33, 
    'x_test_automated_from_playwright__mutmut_34': x_test_automated_from_playwright__mutmut_34, 
    'x_test_automated_from_playwright__mutmut_35': x_test_automated_from_playwright__mutmut_35, 
    'x_test_automated_from_playwright__mutmut_36': x_test_automated_from_playwright__mutmut_36, 
    'x_test_automated_from_playwright__mutmut_37': x_test_automated_from_playwright__mutmut_37, 
    'x_test_automated_from_playwright__mutmut_38': x_test_automated_from_playwright__mutmut_38, 
    'x_test_automated_from_playwright__mutmut_39': x_test_automated_from_playwright__mutmut_39, 
    'x_test_automated_from_playwright__mutmut_40': x_test_automated_from_playwright__mutmut_40, 
    'x_test_automated_from_playwright__mutmut_41': x_test_automated_from_playwright__mutmut_41, 
    'x_test_automated_from_playwright__mutmut_42': x_test_automated_from_playwright__mutmut_42, 
    'x_test_automated_from_playwright__mutmut_43': x_test_automated_from_playwright__mutmut_43, 
    'x_test_automated_from_playwright__mutmut_44': x_test_automated_from_playwright__mutmut_44, 
    'x_test_automated_from_playwright__mutmut_45': x_test_automated_from_playwright__mutmut_45, 
    'x_test_automated_from_playwright__mutmut_46': x_test_automated_from_playwright__mutmut_46, 
    'x_test_automated_from_playwright__mutmut_47': x_test_automated_from_playwright__mutmut_47, 
    'x_test_automated_from_playwright__mutmut_48': x_test_automated_from_playwright__mutmut_48, 
    'x_test_automated_from_playwright__mutmut_49': x_test_automated_from_playwright__mutmut_49
}

def test_automated_from_playwright(*args, **kwargs):
    result = _mutmut_trampoline(x_test_automated_from_playwright__mutmut_orig, x_test_automated_from_playwright__mutmut_mutants, *args, **kwargs)
    return result 

test_automated_from_playwright.__signature__ = _mutmut_signature(x_test_automated_from_playwright__mutmut_orig)
x_test_automated_from_playwright__mutmut_orig.__name__ = 'x_test_automated_from_playwright'




def x_test_update_profile__mutmut_orig(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_1(page: Page):
    page.goto("XXhttp://localhost:8000/XX")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_2(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("XXlinkXX", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_3(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="XXLoginXX").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_4(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link",).click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_5(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("XXEnter your usernameXX").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_6(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("XXtravisXX")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_7(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("XXEnter your passwordXX").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_8(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("XXpassword1234!@#$XX")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_9(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("XXbuttonXX", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_10(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="XXContinueXX").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_11(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button",).click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_12(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("XXlinkXX", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_13(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="XXUpdate ProfileXX").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_14(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link",).click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_15(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("XXProfile picture:XX").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_16(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "XXfilmproject/media/profile_pictures/dummyPFP.jpgXX"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_17(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("XXbuttonXX", name="Update").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_18(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="XXUpdateXX").click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_19(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button",).click()
    page.wait_for_timeout(2000)


def x_test_update_profile__mutmut_20(page: Page):
    page.goto("http://localhost:8000/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Enter your username").fill("travis")
    page.get_by_placeholder("Enter your password").fill("password1234!@#$")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Update Profile").click()
    page.get_by_label("Profile picture:").set_input_files(
        "filmproject/media/profile_pictures/dummyPFP.jpg"
    )
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(2001)

x_test_update_profile__mutmut_mutants = {
'x_test_update_profile__mutmut_1': x_test_update_profile__mutmut_1, 
    'x_test_update_profile__mutmut_2': x_test_update_profile__mutmut_2, 
    'x_test_update_profile__mutmut_3': x_test_update_profile__mutmut_3, 
    'x_test_update_profile__mutmut_4': x_test_update_profile__mutmut_4, 
    'x_test_update_profile__mutmut_5': x_test_update_profile__mutmut_5, 
    'x_test_update_profile__mutmut_6': x_test_update_profile__mutmut_6, 
    'x_test_update_profile__mutmut_7': x_test_update_profile__mutmut_7, 
    'x_test_update_profile__mutmut_8': x_test_update_profile__mutmut_8, 
    'x_test_update_profile__mutmut_9': x_test_update_profile__mutmut_9, 
    'x_test_update_profile__mutmut_10': x_test_update_profile__mutmut_10, 
    'x_test_update_profile__mutmut_11': x_test_update_profile__mutmut_11, 
    'x_test_update_profile__mutmut_12': x_test_update_profile__mutmut_12, 
    'x_test_update_profile__mutmut_13': x_test_update_profile__mutmut_13, 
    'x_test_update_profile__mutmut_14': x_test_update_profile__mutmut_14, 
    'x_test_update_profile__mutmut_15': x_test_update_profile__mutmut_15, 
    'x_test_update_profile__mutmut_16': x_test_update_profile__mutmut_16, 
    'x_test_update_profile__mutmut_17': x_test_update_profile__mutmut_17, 
    'x_test_update_profile__mutmut_18': x_test_update_profile__mutmut_18, 
    'x_test_update_profile__mutmut_19': x_test_update_profile__mutmut_19, 
    'x_test_update_profile__mutmut_20': x_test_update_profile__mutmut_20
}

def test_update_profile(*args, **kwargs):
    result = _mutmut_trampoline(x_test_update_profile__mutmut_orig, x_test_update_profile__mutmut_mutants, *args, **kwargs)
    return result 

test_update_profile.__signature__ = _mutmut_signature(x_test_update_profile__mutmut_orig)
x_test_update_profile__mutmut_orig.__name__ = 'x_test_update_profile'




@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_USE_TLS=False,
    EMAIL_HOST="localhost",
    EMAIL_PORT=1025,
)
def test_user_registration(live_server, transactional_db):
    user = "testuser"
    email = "testuser@example.com"
    password = "PasswordTest123#@!"

    mail.outbox = []  # Clear any existing emails

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the registration page
        page.goto(live_server.url)
        page.get_by_role("link", name="Login").click()
        page.get_by_role("link", name="Sign Up").click()

        # Fill the registration form
        page.fill('input[name="username"]', user)
        page.fill('input[name="email"]', email)
        page.fill('input[name="password1"]', password)
        page.fill('input[name="password2"]', password)
        page.get_by_role("button", name="Continue").click()

        # Wait for the page to load and network requests to finish
        page.wait_for_load_state("networkidle")

        # Ensure the email was sent
        assert len(mail.outbox) == 1, "No email was sent"
        activation_email = mail.outbox[0]
        assert activation_email.subject == "Activate your account."

        # Retrieve activation link from the email
        server_url = re.escape(live_server.url)
        activation_link = re.search(
            rf"{server_url}/activate/([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)/",
            activation_email.body,
        )
        assert (
            activation_link is not None
        ), "Activation link not found in email."

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
