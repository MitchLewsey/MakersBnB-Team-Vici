# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/users_seeds.sql")

    # # Insert a new record
    db_connection.execute("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)", ["Allen Iverson", "allen@iverson.com", "allen123"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM users")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "Fred Smith", "email": "fred@smith.com", "password_hash": "fred123" },
        {"id": 2, "name": "Sam Jones", "email": "sam@jones.com", "password_hash": "sam123" },
        {"id": 3, "name": "Matthew Wiggans", "email": "matthew@wiggans.com", "password_hash": "matthew123" },
        {"id": 4, "name": "Dani Rojas", "email": "dani@rojas.com", "password_hash": "dani123" },
        {"id": 5, "name": "Allen Iverson", "email": "allen@iverson.com", "password_hash": "allen123" }

    ]
