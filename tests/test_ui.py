from playwright.sync_api import expect
#page.goto(...)       # перейти на страницу
#page.locator(...)    # найти элемент
#page.click(...)      # нажать
#page.fill(...)       # ввести текст

def test_user_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

def test_user_login_via_role(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")

def test_user_login_via_id(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
    "https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_user_without_login_credentials(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("")
    page.locator('[data-test="password"]').fill("")
    page.locator('[data-test="login-button"]').click()
    expect(page.locator(
        '[data-test="error"]')).to_have_text(
        "Epic sadface: Username is required"
    )

def test_user_login_invalid_username(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("invalid_username")
    page.locator('[data-test="password"]').fill("test_password")
    page.locator('[data-test="login-button"]').click()
    expect(page.locator(
        '[data-test="error"]')).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_user_login_invalid_password(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("invalid_password")
    page.locator('[data-test="login-button"]').click()
    expect(page.locator(
        '[data-test="error"]')).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

def test_products_existing(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")
    expect(page.get_by_text("Sauce Labs Fleece Jacket")).to_have_text("Sauce Labs Fleece Jacket")
    expect(page.locator('[data-test="inventory-item-sauce-labs-fleece-jacket-img"]')).to_be_visible()

def test_images_existing(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    expect(page.get_by_alt_text("Sauce Labs Fleece Jacket")).to_be_visible()

def test_add_product_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html")
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text("Sauce Labs Fleece Jacket")

def test_price_jacket(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    product = page.locator('[data-test="inventory-item"]').filter(
        has_text="Sauce Labs Fleece Jacket"
    )
    expect(product.locator(".inventory_item_price")).to_have_text("$49.99")

def test_price_jacket_via_get_by_text(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Sauce Labs Fleece Jacket")).to_be_visible()

def test_price_low_to_high(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    page.locator('[data-test="product-sort-container"]').select_option("lohi")
    expect(page.locator('[data-test="product-sort-container"]')).to_have_value("lohi")
    expect(page.locator('[data-test="active-option"]')).to_have_text("Price (low to high)")

def test_screenshot(page):
    page.goto("https://www.saucedemo.com/")
    page.screenshot(path="login_page.png")

def test_current_url(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    current_url = page.url
    print(current_url)

def test_inner_title(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    title = page.get_by_text("Products")
    text = title.inner_text()
    print(text)

def test_username_input_value(page):
    page.goto("https://www.saucedemo.com/")
    username = page.locator('[data-test="username"]')
    username.fill("standard_user")
    value = username.input_value()
    print(value)

def test_get_product_image_attribute(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    image = page.get_by_alt_text("Sauce Labs Fleece Jacket")
    src = image.get_attribute("src")
    print(src)
