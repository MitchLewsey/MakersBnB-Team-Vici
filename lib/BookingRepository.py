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
    
    def hostings_for_host(self, owner_id):
        return self._connection.execute(
            """
            SELECT
            b.id AS booking_id,
            b.start_date,
            b.end_date,
            b.checkout_date,
            b.booking_price,
            l.id AS listing_id,
            l.title AS listing_title,
            l.county AS listing_county,
            l.img_url AS listing_img_url,            
            u.id AS guest_id,
            u.name AS guest_name,
            u.email AS guest_email
            FROM bookings b
            JOIN listings l ON l.id = b.listing_id
            JOIN users u ON u.id = b.guest_id
            WHERE l.owner_id = %s
            ORDER BY b.id;
            """,
            [owner_id]
        )

    
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
    
    def find_by_guest_id(self, guest_id):
        bookings_table = self._connection.execute(""" SELECT
            l.title,
            l.img_url,
            l.listing_description,
            l.county,
            b.id,
            b.guest_id,
            b.start_date,
            b.end_date,
            b.checkout_date,
            b.booking_price
            FROM bookings AS b
            JOIN listings AS l ON b.listing_id = l.id
            WHERE b.guest_id = %s
            ORDER by b.id;      
        """,[guest_id])
        return bookings_table
    
    def unavailable_ranges_for_listing(self, listing_id):
        rows = self._connection.execute(
            """
            SELECT start_date, end_date
            FROM bookings
            WHERE listing_id = %s
            ORDER BY start_date;
            """,
            [listing_id]
        )
        return rows