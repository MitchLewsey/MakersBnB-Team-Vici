from lib.user_repository import *

def test_get_all_users(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'Fred Smith', 'fred@smith.com', 'fred123'),
        User(2, 'Sam Jones', 'sam@jones.com', 'sam123'),
        User(3, 'Matthew Wiggans', 'matthew@wiggans.com', 'matthew123'),
        User(4, 'Dani Rojas', 'dani@rojas.com', 'dani123')
    ]

def test_get_user_from_email(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email('sam@jones.com')
    assert user == User(2, 'Sam Jones', 'sam@jones.com', 'sam123')

def test_get_user_password(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    password = repository.get_user_password_hash('sam@jones.com')
    assert password == 'sam123'

def test_create_user(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, 'Paul McCartney', 'paul@beatles.net', 'paul123'))
    users = repository.all()
    assert users == [
        User(1, 'Fred Smith', 'fred@smith.com', 'fred123'),
        User(2, 'Sam Jones', 'sam@jones.com', 'sam123'),
        User(3, 'Matthew Wiggans', 'matthew@wiggans.com', 'matthew123'),
        User(4, 'Dani Rojas', 'dani@rojas.com', 'dani123'),
        User(5, 'Paul McCartney', 'paul@beatles.net', 'paul123')
    ]

def test_update_user_by_email(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    user_to_update = User(None, 'Frederick Smith', 'fred@smith.com', 'newpass456')
    repository.update_user(user_to_update)
    updated_user = repository.find_by_email('fred@smith.com')
    assert updated_user.name == 'Frederick Smith'
    assert updated_user.password_hash == 'newpass456'

def test_delete_user_by_email(db_connection):
    db_connection.seed("seeds/users_seeds.sql")
    repository = UserRepository(db_connection)
    repository.delete_user('sam@jones.com')
    users = repository.all()
    assert users == [
        User(1, 'Fred Smith', 'fred@smith.com', 'fred123'),
        User(3, 'Matthew Wiggans', 'matthew@wiggans.com', 'matthew123'),
        User(4, 'Dani Rojas', 'dani@rojas.com', 'dani123')
    ]