# This is an example of how to use the DatabaseConnection class
from datetime import date

"""
When I seed the database
I get bookings back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql") 


    # # Insert a new record
    # db_connection.execute("INSERT INTO booking (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM bookings")

    # Assert that the results are what we expect
   

    assert result == [
        {
            "id": 1,
            "status": "Requested",
            "guest_id": 1,
            "listing_id": 3,
            "start_date": date(2026, 1, 20),
            "end_date": date(2026, 1, 21),
            "checkout_date": date(2026, 1, 20),
            "booking_price": 50.00,
        },
        {
            "id": 2,
            "status": "Approved",
            "guest_id": 2,
            "listing_id": 2,
            "start_date": date(2026, 1, 28),
            "end_date": date(2026, 1, 29),
            "checkout_date": date(2026, 1, 15),
            "booking_price": 77.00,
        },
        {
            "id": 3,
            "status": "Approved",
            "guest_id": 3,
            "listing_id": 1,
            "start_date": date(2026, 2, 10),
            "end_date": date(2026, 2, 11),
            "checkout_date": date(2026, 1, 18),
            "booking_price": 100.00,
        },
        {
            "id": 4,
            "status": "Requested",
            "guest_id": 1,
            "listing_id": 3,
            "start_date": date(2026, 1, 25),
            "end_date": date(2026, 1, 26),
            "checkout_date": date(2026, 1, 19),
            "booking_price": 50.00,
        },
        {
            "id": 5,
            "status": "Requested",
            "guest_id": 2,
            "listing_id": 3,
            "start_date": date(2026, 1, 21),
            "end_date": date(2026, 1, 22),
            "checkout_date": date(2026, 1, 20),
            "booking_price": 50.00,
        },
    ]