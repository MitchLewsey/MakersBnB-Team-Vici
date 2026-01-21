from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection

"""
List out all listings when calling GET /listings
"""
def test_get_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/listings")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Price per night: 100.50 County: Hertfordshire About this MakersBnB: lovely stay with breakfast included",
        "Price per night: 3000 County: Edinburgh About this MakersBnB: huge castle, tennis courts"
    ])
    title_tags = page.locator("h2")
    expect(title_tags).to_have_text([
        "2 bed apartment",
        "15 bed castle"
    ])
    expect(page.get_by_alt_text("An image of the MakersBNB"))
"""
Get listing by ID returns only the given list
"""
def test_get_listing_by_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/listings")
    page.click("text='2 bed apartment'")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text("2 bed apartment")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Price per night: 100.50 County: Hertfordshire About this MakersBnB: lovely stay with breakfast included"
    ])