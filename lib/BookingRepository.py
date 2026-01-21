from lib.bookings import *
from lib.database_connection import * 

class BookingRepository():
    def __init__(self, db_connection):
        self._connection = db_connection

    def all(self): 
        bookings_table = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in bookings_table: 
            item = Bookings(row['id'],
                            row['guest_id'],
                            row['listing_id'],
                            row['start_date'],
                            row['end_date'],
                            row['checkout_date'],
                            row['booking_price']
                            )
            bookings.append(item)
        return bookings
    
    def find_by_id(self, booking_id):
        booking_rows = self._connection.execute('SELECT * FROM bookings WHERE id =%s', [booking_id])
        row = booking_rows[0]
        return Bookings(row['id'],
                            row['guest_id'],
                            row['listing_id'],
                            row['start_date'],
                            row['end_date'],
                            row['checkout_date'],
                            row['booking_price']
                            )