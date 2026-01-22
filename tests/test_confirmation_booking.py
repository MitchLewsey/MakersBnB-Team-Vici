from playwright.sync_api import Page, expect
from flask import session

def test_get_booking_confirmation(db_connection, page, test_web_address):
    db_connection.seed("seeds/bookings_seeds.sql")
    page.goto(f"http://{test_web_address}/booking_confirmation")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text(
        "Your booking request has been successful"
    )