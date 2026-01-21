def login(client, email, password):
    return client.post(
        "/login",
        data={"email": email, "password": password},
        follow_redirects=True,  # works whether login returns 200 or redirect
    )

def seed_all(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

def test_login_success_sets_session_and_allows_hostings(web_client, db_connection):
    seed_all(db_connection)

    response = login(web_client, "matthew@wiggans.com", "matthew123")
    assert response.status_code == 200

    with web_client.session_transaction() as sess:
        assert sess.get("user_id") == 3

    hostings_response = web_client.get("/hostings")
    assert hostings_response.status_code == 200

    html = hostings_response.data.decode("utf-8")
    assert "My Hostings" in html
    assert "40 bed castle" in html

def test_hostings_redirects_to_login_when_not_logged_in(web_client, db_connection):
    seed_all(db_connection)
    response = web_client.get("/hostings", follow_redirects=False)
    assert response.status_code in (301, 302)
    assert "/login" in response.headers["Location"]

def test_hostings_shows_only_bookings_for_hosts_listings(web_client, db_connection):
    seed_all(db_connection)
    login(web_client, "matthew@wiggans.com", "matthew123")
    html = web_client.get("/hostings").data.decode("utf-8")
    assert "40 bed castle" in html
    assert "15 bed castle" not in html