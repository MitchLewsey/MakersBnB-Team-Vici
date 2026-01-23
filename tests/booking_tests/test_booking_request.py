from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.bookings import Bookings
from lib.BookingRepository import BookingRepository
from playwright.sync_api import Page, expect
#TEST 1 - test that create() inserts a booking and returns a Booking object

def test_create_booking(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

    repo = BookingRepository(db_connection)

    booking = Bookings(
        None,
        "Requested",
        1,
        1,
        "2026-01-20",
        "2026-01-20",
        "2026-01-20",
        50.00
    )

    created = repo.create(booking)

    assert created.id is not None
    assert created.status == "Requested"
    assert created.guest_id == 1
    assert created.listing_id == 1
    assert created.start_date == "2026-01-20"
    assert created.end_date == "2026-01-20"
    assert created.checkout_date == "2026-01-20"
    assert created.price == 50.00

#TEST 2 - test the success message in the route test

# def test_booking_route_returns_success_message(web_client):
#     response = web_client.post('/bookings', data={
#         'guest_id': '1',
#         'listing_id': '1',
#         'start_date': '2026-01-20',
#         'end_date': '2026-01-20',
#         'checkout_date': '2026-01-20',
#         'booking_price': '50.00'
#     })

#     assert response.status_code == 200
#     assert "Your booking request has been submitted successfully." in response.get_data(as_text=True)

#TEST 3 - Test for past date 

#TEST 4 - N/A
"""
View booking request page for a specific listing
"""
def test_get_booking_request_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/book?id=1")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("MakersBnB")

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Request to book: 2 bed apartment")

    p_tags = page.locator("p")
    expect(p_tags).to_have_text([
        "Location: Hertfordshire",
        "Price per night: £100.50"
    ])

    expect(page.locator("input[name=listing_id]")).to_have_attribute("value", "1")
    expect(page.locator("input[name=booking_price]")).to_have_attribute("value", "100.50")
    expect(page.locator("input[name=start_date]")).to_be_visible()
    expect(page.locator("input[name=end_date]")).to_be_visible()




"""
Submitting a valid booking request posts the booking and redirects appropriately
"""
def test_create_booking_request_success(db_connection, page, test_web_address):
    db_connection.seed("seeds/listings_seeds.sql")
    page.goto(f"http://{test_web_address}/book?id=1")


    page.fill("input[name=start_date]", "2026-02-01")
    page.fill("input[name=end_date]", "2026-02-01")
    page.click("text='Confirm Booking Request'")