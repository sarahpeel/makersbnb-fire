from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("Prepare for your next adventure")

"""
we can render the register page
"""
def test_get_register(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    page.goto(f"http://{test_web_address}/register")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Register a new account")

"""
we register successfully on the register page
"""

def test_register_new_user_success(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    page.goto(f"http://{test_web_address}/register")
    page.fill("input[name='username']", "Dewi")

    page.locator("#register_btn").click()

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Login")

    page.fill("input[name='username']", "Dewi")
    page.locator("#login_btn").click()

    successful_login = page.locator(".t-title")
    expect(successful_login).to_have_text("You have successfully logged in.")
    username_text = page.locator(".t-username")
    expect(username_text).to_have_text("Your username: Dewi")

"""
we can render a listings page
with a list of all places
"""
def test_show_all_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    page.goto(f"http://{test_web_address}/listings")
    p_tag = page.locator("h1")
    expect(p_tag).to_have_text("Current Listings")
