from lib.listing import Listing
from playwright.sync_api import Page, expect


def test_listings_all(db_connection, web_client):
    db_connection.seed("seeds/listings_seeds.sql")
    response = web_client.get("/listings")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == [Listing(1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'), Listing(2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam')]



