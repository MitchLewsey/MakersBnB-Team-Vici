from datetime import date

def seed_all(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    db_connection.seed("seeds/listings_seeds.sql")
    db_connection.seed("seeds/bookings_seeds.sql")

def login_as(web_client, email, password):
    return web_client.post(
        "/login",
        data={"email": email, "password": password},
        follow_redirects=True
    )

def test_checkout_page_requires_login(web_client, db_connection):
    seed_all(db_connection)

    response = web_client.get("/listings/1/checkout", follow_redirects=False)
    assert response.status_code in (301, 302)
    assert "/login" in response.headers["Location"]


def test_checkout_page_renders_listing_details_when_logged_in(web_client, db_connection):
    seed_all(db_connection)

    login_as(web_client, "fred@smith.com", "fred123")

    response = web_client.get("/listings/1/checkout")
    assert response.status_code == 200

    html = response.data.decode("utf-8")
    assert "Request to book" in html
    assert "2 bed apartment" in html  # listing title from seeds
    assert "Hertfordshire" in html    # county from seeds


def test_post_bookings_creates_booking_request(web_client, db_connection):
    seed_all(db_connection)

    login_as(web_client, "fred@smith.com", "fred123")

    response = web_client.post(
        "/bookings",
        data={
            "listing_id": 1,
            "start_date": "2026-03-10",
            "end_date": "2026-03-12"
        },
        follow_redirects=False
    )

    assert response.status_code in (301, 302)

    rows = db_connection.execute(
        """
        SELECT * FROM bookings
        WHERE guest_id = %s AND listing_id = %s
          AND start_date = %s AND end_date = %s
        """,
        [1, 1, date(2026, 3, 10), date(2026, 3, 12)]
    )
    assert len(rows) == 1
    assert rows[0]["booking_price"] is not None
    assert rows[0]["checkout_date"] is not None


def test_post_bookings_requires_login(web_client, db_connection):
    seed_all(db_connection)

    response = web_client.post(
        "/bookings",
        data={
            "listing_id": 1,
            "start_date": "2026-03-10",
            "end_date": "2026-03-12"
        },
        follow_redirects=False
    )
    assert response.status_code in (301, 302)
    assert "/login" in response.headers["Location"]


def test_post_bookings_rejects_end_date_before_start_date(web_client, db_connection):
    seed_all(db_connection)

    login_as(web_client, "fred@smith.com", "fred123")

    response = web_client.post(
        "/bookings",
        data={
            "listing_id": 1,
            "start_date": "2026-03-12",
            "end_date": "2026-03-10"
        },
        follow_redirects=False
    )

    assert response.status_code == 400
    body = response.data.decode("utf-8").lower()
    assert "end date" in body or "check-out" in body