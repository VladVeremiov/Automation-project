import json
import uuid
from playwright.sync_api import expect

def test_register(page):
    unique_id = str(uuid.uuid4())[:8]
    email = f"test_user_{unique_id}@example.com"
    page.goto("https://dojo.upexgalaxy.com/register")
    page.get_by_test_id("register-name-input").fill("Test User")
    page.get_by_test_id("register-email-input").fill(email)
    page.get_by_test_id("register-password-input").fill("Test123!")
    page.get_by_test_id("register-confirm-password-input").fill("Test123!")
    page.get_by_test_id("register-submit-button").click()
    expect(page).to_have_url(
        "https://dojo.upexgalaxy.com/dashboard"
    )



def test_user_login(page):
    with open("test_data/users.json") as file:
        users = json.load(file)

    email = users["valid_user"]["email"]
    password = users["valid_user"]["password"]

    page.goto("https://dojo.upexgalaxy.com/login/")
    page.get_by_test_id("login-email-input").fill(email)
    page.get_by_test_id("login-password-input").fill(password)
    page.get_by_test_id("login-submit-button").click()

    expect(page).to_have_url(
        "https://dojo.upexgalaxy.com/dashboard")