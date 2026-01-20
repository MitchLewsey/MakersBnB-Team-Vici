# from lib.album import Album
# from lib.album_repository import AlbumRepository
# from playwright.sync_api import Page, expect

"""
WHEN I make a GET request to /listings&id=1 

THEN the http response status is 200 

"""

# def test_listing(db_connection, web_client):
#     db_connection.seed("seeds/listings_seeds.sql")
#     response = web_client.get("/listings/1")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "Listing(1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b')"


# def test_get_all_albums(page, test_web_address, db_connection):
#     db_connection.seed("seeds/albums_table.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     div_tags = page.locator("div")
#     expect(div_tags).to_have_text([
#         "Title: Ride The Fader\nReleased:1996",
#         "Title: Songs From the Choirgirl Hotel\nReleased: 1998",
#         "Title: Rubber Soul\nReleased: 1965",
#         "Title: Gone Glimmering\nReleased: 1993",
#      ])