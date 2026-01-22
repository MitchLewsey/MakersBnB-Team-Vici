def seed_all(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")


def test_signup_creates_user_and_sets_session(web_client, db_connection):
    seed_all(db_connection)

    resp = web_client.post(
        "/signup",
        data={"name": "New User", "email": "new@user.com", "password": "pass123"},
        follow_redirects=False
    )

    assert resp.status_code in (301, 302)

    rows = db_connection.execute("SELECT * FROM users WHERE email = %s", ["new@user.com"])
    assert len(rows) == 1

    new_user_id = rows[0]["id"]
    with web_client.session_transaction() as sess:
        assert sess.get("user_id") == new_user_id


def test_signup_rejects_duplicate_email(web_client, db_connection):
    seed_all(db_connection)

    resp = web_client.post(
        "/signup",
        data={"name": "Someone", "email": "fred@smith.com", "password": "anything"},
        follow_redirects=False
    )

    assert resp.status_code == 400

    with web_client.session_transaction() as sess:
        assert sess.get("user_id") is None


def test_get_signup_redirects_if_logged_in(web_client, db_connection):
    seed_all(db_connection)

    web_client.post(
        "/login",
        data={"email": "matthew@wiggans.com", "password": "matthew123"},
        follow_redirects=True
    )

    resp = web_client.get("/signup", follow_redirects=False)
    assert resp.status_code in (301, 302)
    assert "/listings" in resp.headers["Location"]