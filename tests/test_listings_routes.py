from playwright.sync_api import Page, expect

"""
List out all listings when calling GET /listings
"""
def test_get_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")

    page.goto(f"http://{test_web_address}/listings")

    titles = page.locator("h2")
    expect(titles).to_have_text([
        "2 bed apartment",
        "15 bed castle",
        "40 bed castle"
    ])

    body = page.locator("body")
    expect(body).to_contain_text("£100.5")
    expect(body).to_contain_text("Hertfordshire")
    expect(body).to_contain_text("lovely stay with breakfast included")
    expect(body).to_contain_text("Edinburgh")


"""
Get listing by ID returns only the given listing
"""
def test_get_listing_by_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")

    page.goto(f"http://{test_web_address}/listings/1")

    expect(page.locator("h1")).to_have_text("Listing details")
    expect(page.locator("body")).to_contain_text("2 bed apartment")
    expect(page.locator("body")).to_contain_text("£100.5")
    expect(page.locator("body")).to_contain_text("Hertfordshire")


"""
Create listing with valid parameters redirects to listing details
"""
def test_create_listing_success_redirect_to_listing_details(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")

    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "fred@smith.com")
    page.fill("input[name=password]", "fred123")
    page.click("button[type=submit]")

    page.goto(f"http://{test_web_address}/listings/new")

    expect(page.locator("h1")).to_have_text("Add a Listing")

    page.fill("input[name=title]", "4 bed house")
    page.fill("input[name=price_per_night]", "250")
    page.fill("input[name=county]", "Buckinghamshire")
    page.fill("input[name=listing_description]", "Spacious 4 bed house in the centre of town")
    page.fill("input[name=img_url]", "https://example.com/house.jpg")

    page.click("button[type=submit]")

    expect(page.locator("body")).to_contain_text("4 bed house")
    expect(page.locator("body")).to_contain_text("Buckinghamshire")