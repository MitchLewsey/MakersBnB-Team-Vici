from playwright.sync_api import Page, expect
from flask import session

def test_login_success(web_client, db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    response = web_client.post('/login', data={
        'email': 'fred@smith.com',
        'password': 'fred123'
    })
    assert response.status_code == 200
    with web_client.session_transaction() as sess:
        assert sess["id"] == 1  # or whatever the user ID is in your seed file

def test_invalid_credentials(web_client, db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    response = web_client.post('/login', data={
        'email': 'fred@smith.com',
        'password': 'fred'
    })
    assert response.status_code == 401
    assert response.data.decode('utf-8') == "Error: Invalid username or password"

def test_blank_username(web_client, db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    response = web_client.post('/login', data={
        'email': '',
        'password': 'fred123'
    })
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Missing username or password"


def test_blank_password(web_client, db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    response = web_client.post('/login', data={
        'email': 'fred@smith.com',
        'password': ''
    })
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Missing username or password"

