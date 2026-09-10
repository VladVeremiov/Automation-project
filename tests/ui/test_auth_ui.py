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

def test_create_task(page):
    with open("test_data/users.json") as file:
        users = json.load(file)

    email = users["valid_user"]["email"]
    password = users["valid_user"]["password"]

    unique_id = str(uuid.uuid4())[:8]
    name_of_task = f"Test_{unique_id}"

    page.goto("https://dojo.upexgalaxy.com/login/")
    page.get_by_test_id("login-email-input").fill(email)
    page.get_by_test_id("login-password-input").fill(password)
    page.get_by_test_id("login-submit-button").click()

    expect(page).to_have_url(
        "https://dojo.upexgalaxy.com/dashboard")
    expect(page.get_by_test_id("new-task-button")).to_be_enabled()

    page.get_by_test_id("new-task-button").click()
    expect(page.get_by_test_id("task-modal")).to_be_visible()
    page.get_by_test_id("task-title-input").fill(name_of_task)
    page.get_by_test_id("task-description-input").fill("Test Description")
    page.get_by_test_id("task-priority-select").click()
    page.get_by_test_id("priority-low").click()
    page.get_by_test_id("task-submit-button").click()

    expect(page.get_by_text(name_of_task)).to_be_visible()

def test_edit_task(page):
    with open("test_data/users.json") as file:
        users = json.load(file)

    email = users["valid_user"]["email"]
    password = users["valid_user"]["password"]

    unique_id = str(uuid.uuid4())[:8]
    name_of_task = f"Test_{unique_id}"

    page.goto("https://dojo.upexgalaxy.com/login/")
    page.get_by_test_id("login-email-input").fill(email)
    page.get_by_test_id("login-password-input").fill(password)
    page.get_by_test_id("login-submit-button").click()

    expect(page).to_have_url(
        "https://dojo.upexgalaxy.com/dashboard")
    expect(page.get_by_test_id("new-task-button")).to_be_enabled()

    page.get_by_test_id("new-task-button").click()
    expect(page.get_by_test_id("task-modal")).to_be_visible()
    page.get_by_test_id("task-title-input").fill(name_of_task)
    page.get_by_test_id("task-description-input").fill("Test Description")
    page.get_by_test_id("task-priority-select").click()
    page.get_by_test_id("priority-low").click()
    page.get_by_test_id("task-submit-button").click()

    expect(page.get_by_text(name_of_task)).to_be_visible()


    card = page.locator("[data-testid^='task-card-']").filter(
        has_text=name_of_task
    )
    menu_button = card.locator("[data-testid^='task-menu-']")
    menu_button.click()

    edit_button = page.locator("[data-testid^='task-edit-']")
    edit_button.click()

    page.get_by_test_id("task-title-input").fill(f"Edited_{name_of_task}")
    page.get_by_test_id("task-description-input").fill("Edited Description")
    page.get_by_test_id("task-priority-select").click()
    page.get_by_test_id("priority-high").click()
    page.get_by_test_id("task-submit-button").click()

    edited_name = f"Edited_{name_of_task}"
    edited_card = page.locator("[data-testid^='task-card-']").filter(
        has_text=edited_name
    )
    expect(edited_card).to_be_visible()
    expect(edited_card.get_by_text(edited_name)).to_be_visible()
    expect(edited_card.get_by_text("Edited Description")).to_be_visible()
    expect(edited_card.locator("[data-testid^='task-priority-']")).to_have_text("high")

def test_delete_task(page):
    with open("test_data/users.json") as file:
        users = json.load(file)

    email = users["valid_user"]["email"]
    password = users["valid_user"]["password"]

    unique_id = str(uuid.uuid4())[:8]
    name_of_task = f"Test_{unique_id}"

    page.goto("https://dojo.upexgalaxy.com/login/")
    page.get_by_test_id("login-email-input").fill(email)
    page.get_by_test_id("login-password-input").fill(password)
    page.get_by_test_id("login-submit-button").click()

    expect(page).to_have_url(
        "https://dojo.upexgalaxy.com/dashboard")
    expect(page.get_by_test_id("new-task-button")).to_be_enabled()

    page.get_by_test_id("new-task-button").click()
    expect(page.get_by_test_id("task-modal")).to_be_visible()
    page.get_by_test_id("task-title-input").fill(name_of_task)
    page.get_by_test_id("task-description-input").fill("Test Description")
    page.get_by_test_id("task-priority-select").click()
    page.get_by_test_id("priority-low").click()
    page.get_by_test_id("task-submit-button").click()

    expect(page.get_by_text(name_of_task)).to_be_visible()

    card = page.locator("[data-testid^='task-card-']").filter(
        has_text=name_of_task
    )
    menu_button = card.locator("[data-testid^='task-menu-']")
    menu_button.click()

    delete_button = page.locator("[data-testid^='task-delete-']")
    page.on("dialog", lambda dialog: dialog.accept())
    delete_button.click()
