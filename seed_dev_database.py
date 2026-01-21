from lib.database_connection import DatabaseConnection

# Run this file to reset your database using the seeds
# ; python seed_dev_database.py

connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed("seeds/users_seeds.sql")
connection.seed("seeds/listings_seeds.sql")
connection.seed("seeds/bookings_seeds.sql")
