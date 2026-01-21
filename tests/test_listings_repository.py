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
   
    # response = web_client.get("/listings")
    # assert response.status_code == 200
    # assert response.data.decode("utf-8") == [Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, 2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam')]



