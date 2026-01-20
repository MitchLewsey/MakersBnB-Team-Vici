from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection

"""
List out all listings when calling GET /listings
"""
def test_get_listings(web_client, db_connection):
    db_connection.seed("seeds/listings_seeds.sql")
    response = web_client.get("/listings")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\
Listing(1, 1, 2 bed apartment, 100.50, Hertfordshire, lovely stay with breakfast included, https://tinyurl.com/ye23e59b)\n\
Listing(2, 2, 15 bed castle, 3000, Edinburgh, huge castle, tennis courts, https://tinyurl.com/mpm6dnam)"

"""
Get listing by ID returns only the given list
"""
def test_get_listing_by_id(web_client, db_connection):
    db_connection.seed("seeds/listings_seeds.sql")
    response = web_client.get("/listings/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Listing(1, 1, 2 bed apartment, 100.50, Hertfordshire, lovely stay with breakfast included, https://tinyurl.com/ye23e59b)"