def test_get_single_listing_page_renders(db_connection, web_client):
    db_connection.seed("seeds/listings_seeds.sql")

    response = web_client.get("/listings/1")

    assert response.status_code == 200
    body = response.data.decode("utf-8")

    assert "2 bed apartment" in body
    assert "£100.5" in body or "100.50" in body
    assert "Hertfordshire" in body
    assert "lovely stay with breakfast included" in body