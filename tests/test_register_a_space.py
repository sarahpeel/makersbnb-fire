from playwright.sync_api import Page, expect

def test_get_register_a_space_h1(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")

    page.goto(f"http://{test_web_address}/login")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Login")

    page.fill("input[name='username']", "Catherine")
    page.locator("#login_btn").click()

    successful_login = page.locator(".t-title")
    expect(successful_login).to_have_text("You have successfully logged in.")
    username_text = page.locator(".t-username")
    expect(username_text).to_have_text("Your username: Catherine")

    page.goto(f"http://{test_web_address}/register_a_space")

    h1_tag = page.locator("#register_title")
    expect(h1_tag).to_have_text("Register a space")


def test_get_register_a_space_form(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")

    page.goto(f"http://{test_web_address}/login")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Login")

    page.fill("input[name='username']", "Catherine")
    page.locator("#login_btn").click()

    successful_login = page.locator(".t-title")
    expect(successful_login).to_have_text("You have successfully logged in.")
    username_text = page.locator(".t-username")
    expect(username_text).to_have_text("Your username: Catherine")

    page.goto(f"http://{test_web_address}/register_a_space")

    h1_tag = page.locator("#register_title")
    expect(h1_tag).to_have_text("Register a space")
    
    page.fill("input[name='name']", "Name of Listing")
    page.fill("input[name='description']", "Description Test")
    page.fill("input[name='location']", "Location Test")
    page.fill("input[name='price']", "12")

    page.click("text=Add Space")

    listing_success = page.locator(".t-title")
    expect(listing_success).to_contain_text("You have successfully registered a listing.")
