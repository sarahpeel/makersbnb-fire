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
    expect(p_tag).to_have_text("This is the homepage.")

"""
we can render the register page
"""
def test_get_register(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    page.goto(f"http://{test_web_address}/register")
    p_tag = page.locator("h1")
    expect(p_tag).to_have_text("Provide the following details to set up your account:")

"""
we register successfully on the register page
"""

def test_register_new_user_success(db_connection, page, test_web_address):
    db_connection.seed("seeds/bnb_db.sql")
    page.goto(f"http://{test_web_address}/register")
    page.fill("input[name='username']", "Dewi")
    page.click("text='Register'")
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("You have successfully registered.")
    para_element = page.locator(".t-username")
    expect(para_element).to_have_text("Your username: Dewi")