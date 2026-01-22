from lib.listing import Listing
from lib.listing_repository import ListingRepository
from lib.database_connection import get_flask_database_connection

def test_listings_all(db_connection):
    db_connection.seed("seeds/listings_seeds.sql")
    listings_repo = ListingRepository(db_connection)
    all_listings = listings_repo.all()
    assert all_listings == [Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, 2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam'), Listing(3, 3, '40 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam')]

def test_find_listing(db_connection):
    db_connection.seed("seeds/listings_seeds.sql")
    listings_repo = ListingRepository(db_connection)
    listing = listings_repo.find(1)
    assert listing == Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')

def test_create_listing(db_connection):
    db_connection.seed("seeds/listings_seeds.sql")
    listings_repo = ListingRepository(db_connection)
    listing = Listing(None, 2, 'studio flat', 50.00, 'Bedfordshire', 'small flat', 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/400780718.jpg?k=983e9752453373f06a2042a591f0d28a47614aa5c1d36ca1986483addc6d1806&o=')
    listings_repo.create(listing)
    all_listings = listings_repo.all()
    assert all_listings == [Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, 2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam'), Listing(3, 3, '40 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam'), Listing(4, 2, 'studio flat', 50.00, 'Bedfordshire', 'small flat', 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/400780718.jpg?k=983e9752453373f06a2042a591f0d28a47614aa5c1d36ca1986483addc6d1806&o=')]



