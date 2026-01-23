from datetime import date
import pytest

def seed_all(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

def login_as(web_client, email, password):
    return web_client.post("/login", data={"email": email, "password": password}, follow_redirects=False)

def test_get_bookings_shows_only_logged_in_users_bookings(web_client, db_connection):
    seed_all(db_connection)

    login_as(web_client, "fred@smith.com", "fred123")

    response = web_client.get("/bookings")
    assert response.status_code == 200

    body = response.data.decode()

    assert "My bookings" in body
    assert "40 bed castle" in body 