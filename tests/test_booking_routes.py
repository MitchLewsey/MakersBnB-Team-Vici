from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection



"""
Get listing by ID returns only the given list
"""


# def test_get_booking_by_id(db_connection, page, test_web_address):
#     db_connection.seed("seeds/listings_seeds.sql")
#     db_connection.seed("seeds/bookings_seeds.sql")
    
#     page.goto(f"http://{test_web_address}/bookings?id=1")
#     page.click("text=40 bed castle")
#     h1_tags = page.locator("h1")
#     expect(h1_tags).to_have_text("Booking Details")
#     h2_tags = page.locator("h2")
    
    # expect(h2_tags).to_have_text(
    #     "40 bed castle"
    # )

"""get booking confirmation"""

def test_get_booking_confirmation(db_connection, page, test_web_address):
    db_connection.seed("seeds/bookings_seeds.sql")

    page.goto(f"http://{test_web_address}/booking_confirmation")
    confirmation_message = page.locator("p")
    expect(confirmation_message).to_have_text("Your booking request has been successful")