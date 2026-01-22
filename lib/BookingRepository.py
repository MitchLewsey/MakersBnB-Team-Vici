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
                            row['status'],
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
                        row['status'],
                            row['guest_id'],
                            row['listing_id'],
                            row['start_date'],
                            row['end_date'],
                            row['checkout_date'],
                            row['booking_price']
                            )
    
    def find_by_guest_id(self, guest_id):
        bookings_table = self._connection.execute('SELECT * FROM bookings WHERE guest_id =%s', [guest_id])
        my_bookings=[]
        for row in bookings_table: 
            item = Bookings(row['id'],
                            row['status'],
                            row['guest_id'],
                            row['listing_id'],
                            row['start_date'],
                            row['end_date'],
                            row['checkout_date'],
                            row['booking_price']
                            )
            my_bookings.append(item)
        return my_bookings
        
    def create(self, booking):
        rows = self._connection.execute(
            """
            INSERT INTO bookings
            (status,guest_id, listing_id, start_date, end_date, checkout_date, booking_price)
            VALUES (%s, %s, %s, %s, %s, %s,%s)
            RETURNING id
            """,
            [
                booking.status,
                booking.guest_id,
                booking.listing_id,
                booking.start_date, 
                booking.end_date,      
                booking.checkout_date, 
                booking.price          
            ]
            )

        row = rows[0]
        booking.id = row["id"]
        return booking

