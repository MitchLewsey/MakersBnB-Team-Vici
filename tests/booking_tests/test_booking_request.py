from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.bookings import Bookings
from lib.BookingRepository import BookingRepository

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

def test_booking_route_returns_success_message(web_client):
    response = web_client.post('/book', data={
        'guest_id': '1',
        'listing_id': '1',
        'start_date': '2026-01-20',
        'end_date': '2026-01-20',
        'checkout_date': '2026-01-20',
        'booking_price': '50.00'
    })

    assert response.status_code == 200
    assert "Your booking request has been submitted successfully." in response.get_data(as_text=True)

#TEST 3 - Test for past date 

#TEST 4 - N/A