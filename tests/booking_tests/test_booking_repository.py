# #Unit and integration tests for the booking repository class 
from lib.BookingRepository import * 
from lib.database_connection import * 
from datetime import date
from decimal import Decimal

def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

    repository = BookingRepository(db_connection)

    bookings = repository.all()

    assert bookings == [
        Bookings(1, 'Requested', 1, 3, date(2026, 1, 20), date(2026, 1, 21), date(2026, 1, 20), Decimal("50.00")),
        Bookings(2, 'Approved', 2, 2, date(2026, 1, 28), date(2026, 1, 29), date(2026, 1, 15), Decimal("77.00")),
        Bookings(3, 'Approved', 3, 1, date(2026, 2, 10), date(2026, 2, 11), date(2026, 1, 18), Decimal("100.00")),
        Bookings(4, 'Requested', 1, 3, date(2026, 1, 25), date(2026, 1, 26), date(2026, 1, 19), Decimal("50.00")),
        Bookings(5, 'Requested', 2, 3, date(2026, 1, 21), date(2026, 1, 22), date(2026, 1, 20), Decimal("50.00")),
    ]

def test_find_booking_by_id(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

    repository = BookingRepository(db_connection)

    booking = repository.find_by_id(3)

    assert booking == Bookings(3, 'Approved', 3, 1, date(2026, 2, 10), date(2026, 2, 11), date(2026, 1, 18), Decimal("100.00"))

def test_create_a_booking(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")
    
    repository = BookingRepository(db_connection)

    booking = Bookings(
    id=None,    
    status='Requested',
    guest_id=1,
    listing_id=2,
    start_date=date(2026, 3, 10),
    end_date=date(2026, 3, 11),
    checkout_date=date(2026, 1, 31),
    booking_price=Decimal("85.00")
    )

    create_booking = repository.create(booking)
    all_bookings = repository.all()

    assert all_bookings == [
        Bookings(1, 'Requested', 1, 3, date(2026, 1, 20), date(2026, 1, 21), date(2026, 1, 20), Decimal("50.00")),
        Bookings(2, 'Approved', 2, 2, date(2026, 1, 28), date(2026, 1, 29), date(2026, 1, 15), Decimal("77.00")),
        Bookings(3, 'Approved', 3, 1, date(2026, 2, 10), date(2026, 2, 11), date(2026, 1, 18), Decimal("100.00")),
        Bookings(4, 'Requested', 1, 3, date(2026, 1, 25), date(2026, 1, 26), date(2026, 1, 19), Decimal("50.00")),
        Bookings(5, 'Requested', 2, 3, date(2026, 1, 21), date(2026, 1, 22), date(2026, 1, 20), Decimal("50.00")),
        Bookings(6, 'Requested', 1, 2, date(2026, 3, 10), date(2026, 3, 11), date(2026, 1, 31), Decimal("85.00"))
    ] 

def test_get_booking_information_by_guest_id(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")
    
    repository = BookingRepository(db_connection)

    response = repository.find_by_guest_id(1)

    assert response == [
        {
            "title": "40 bed castle",
            "img_url": "https://tinyurl.com/mpm6dnam",
            "listing_description": "huge castle, tennis courts",
            "county": "Edinburgh",
            "id": 1,
            "guest_id": 1,
            "start_date": date(2026, 1, 20),
            "end_date": date(2026, 1, 21),
            "checkout_date": date(2026, 1, 20),
            "booking_price": Decimal("50.00")
        },
        {
            "title": "40 bed castle",
            "img_url": "https://tinyurl.com/mpm6dnam",
            "listing_description": "huge castle, tennis courts",
            "county": "Edinburgh",
            "id": 4,
            "guest_id": 1,
            "start_date": date(2026, 1, 25),
            "end_date": date(2026, 1, 26),
            "checkout_date": date(2026, 1, 19),
            "booking_price": Decimal("50.00")
        }
    ]