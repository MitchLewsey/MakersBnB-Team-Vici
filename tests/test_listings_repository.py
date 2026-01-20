from lib.listing import Listing
from lib.listing_repository import ListingRepository
from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection

def test_listings_all(db_connection, web_client):
    db_connection.seed("seeds/listings_seeds.sql")
    listing = ListingRepository(db_connection)

    all_listing = listing.all()
    assert all_listing == [Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, 2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam')]

   
   
    # response = web_client.get("/listings")
    # assert response.status_code == 200
    # assert response.data.decode("utf-8") == [Listing(1, 1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, 2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam')]



