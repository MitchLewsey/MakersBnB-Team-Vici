# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get bookings back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bookings_seeds.sql")

    # # Insert a new record
    # db_connection.execute("INSERT INTO booking (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM bookings")

    # Assert that the results are what we expect
    assert result == [
    {
        "id": 1,
        "guest_id": 1,
        "listing_id": 3,
        "start_date": "2026-01-20",
        "end_date": "2026-01-21",
        "checkout_date": "2026-01-20",
        "booking_price": 50.00
    },
    {
        "id": 2,
        "guest_id": 2,
        "listing_id": 2,
        "start_date": "2026-01-28",
        "end_date": "2026-01-29",
        "checkout_date": "2026-01-15",
        "booking_price": 77.00
    },
    {
        "id": 3,
        "guest_id": 3,
        "listing_id": 1,
        "start_date": "2026-02-10",
        "end_date": "2026-02-11",
        "checkout_date": "2026-01-18",
        "booking_price": 100.00
    },
    {
        "id": 4,
        "guest_id": 1,
        "listing_id": 3,
        "start_date": "2026-01-25",
        "end_date": "2026-01-26",
        "checkout_date": "2026-01-19",
        "booking_price": 50.00
    },
    {
        "id": 5,
        "guest_id": 2,
        "listing_id": 3,
        "start_date": "2026-01-21",
        "end_date": "2026-01-22",
        "checkout_date": "2026-01-20",
        "booking_price": 50.00
    }
]
