import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.listing_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Route's Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

#listings 

@app.route('/listings', methods=['GET'])
def get_all_listings():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listings = listings_repo.all()
    return render_template('listings/index.html', listings=listings)

@app.route('/listings/<id>', methods=['GET'])
def get_single_listing(id):
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listing = listings_repo.find(id)
    if listing is None:
        return "Sorry, that listing does not exist.", 404
    else: 
    # # return f"{single_listing}"
        return render_template('listings_details.html', listing=listing)
## Login route including validation steps

@app.route('/login', methods=['POST'])
def login():
    
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return "Missing username or password", 400
    
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT * FROM users WHERE email = %s AND password_hash = %s", [email, password])

    if len(rows) > 0:
        return render_template("test_listings.html"), 200
    else:
        return "Error: Invalid username or password", 401

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
