from lib.database_connection import get_flask_database_connection

def test_booking_valid_request(db_connection, web_client):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

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

    # connection = get_flask_database_connection(app) 
    # rows = connection.execute( 
    #     "SELECT * FROM bookings WHERE listing_id = %s AND start_date = %s", 
    #     ['1', '2026-01-20']   
    # )
    # assert len(rows) == 1

# def test_book_invalid_request_missing_date(db_connection, web_client):
#     db_connection.seed("seeds/users_seeds.sql")
#     db_connection.seed("seeds/listings_seeds.sql")
#     db_connection.seed("seeds/bookings_seeds.sql")

#     response = web_client.post('/book', data={
#         'guest_id': '1',
#         'listing_id': '1',
#         'start_date': '', #invalid date-type
#         'end_date': '2026-01-20',
#         'checkout_date': '2026-01-20',
#         'booking_price': '50.00'
#         })

#     assert response.status_code == 401
#     assert "Error: missing or invalid date" in response.get_data(as_text=True)