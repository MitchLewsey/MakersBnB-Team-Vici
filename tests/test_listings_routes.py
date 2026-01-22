from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection

"""
List out all listings when calling GET /listings
used .to_contain_text method for this test as the section 
elements throw in new lines that cause the test to fail
"""

def test_get_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/listings")
    section_tags = page.locator("section")
    expect(section_tags).to_contain_text([
        "Price per night: £100.50",
        "County: Hertfordshire",
        "About this MakersBnB: lovely stay with breakfast included",
        "Price per night: £3000",
        "County: Edinburgh",
        "About this MakersBnB: huge castle, tennis courts",
        "Price per night: £3000",
        "County: Edinburgh",
        "About this MakersBnB: huge castle, tennis courts"
      ])
    title_tags = page.locator("h2")
    expect(title_tags).to_have_text([
        "2 bed apartment",
        "15 bed castle",
        "40 bed castle"
    ])
    expect(page.get_by_alt_text("An image of the MakersBNB"))
"""
Get listing by ID returns only the given listing
"""
def test_get_listing_by_id(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/listings")
    page.click("text='2 bed apartment'")
    h2_tags = page.locator("h2")
    expect(h2_tags).to_have_text("2 bed apartment")
    section_tags = page.locator("section")
    expect(section_tags).to_have_text([
        "Price per night: £100.50", 
        "County: Hertfordshire", 
        "About this MakersBnB: lovely stay with breakfast included"
    ])

"""
Create listing with valid parameters creates a listing in the database
And returns the user to details page of their listing
"""
# def test_create_listing_success_redirect_to_listing_details(db_connection, page, test_web_address):
#     db_connection.seed("seeds/listings_seeds.sql")
#     page.goto(f"http://{test_web_address}/listings")
#     page.click("text='Add Listing'")
#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text("Add a Listing")
#     page.fill("input[name=owner_id]", "1")
#     page.fill("input[name=title]", "4 bed house")
#     page.fill("input[name=price_per_night]", "250.00")
#     page.fill("input[name=county]", "Buckinghamshire")
#     page.fill("input[name=listing_description]", "Spacious 4 bed house in the centre of town")
#     page.fill("input[name=img_url]", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/d6/a1/6b/buckingham-palace.jpg?w=800&h=500&s=1")
    
        
#     page.click("text='Submit Listing'")
#     h2_tags = page.locator("h2")
#     expect(h2_tags).to_have_text("4 bed house")