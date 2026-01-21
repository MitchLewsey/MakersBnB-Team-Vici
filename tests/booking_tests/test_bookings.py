from lib.bookings import * 
from datetime import date
from decimal import Decimal
#Tests for the bookings class

def test_bookings_class_is_setup():
    
    booking = Bookings(1,'Requested',2,2,date(2026,1,11),date(2026,1,12),date(2026,1,8),150.00)
    
    assert booking.id == 1
    assert booking.status == 'Requested' 
    assert booking.guest_id == 2
    assert booking.listing_id == 2
    assert booking.start_date == date(2026, 1, 11)
    assert booking.end_date == date(2026, 1, 12)
    assert booking.checkout_date == date(2026, 1, 8)
    assert booking.price == Decimal("150.00")

"""

We can compare two identical bookings
And have them be equal
"""
def test_booksings_are_equal():
    bookings1 =  Bookings(1,'Requested',2,2,date(2026,1,11),date(2026,1,12),date(2026,1,8),Decimal("150.00"))
    bookings2 =  Bookings(1,'Requested',2,2,date(2026,1,11),date(2026,1,12),date(2026,1,8),Decimal("150.00"))
    assert bookings1 == bookings2
    
