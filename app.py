import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.BookingRepository import BookingRepository
from lib.listing_repository import *
from lib.BookingRepository import *

# Create a new Flask app
app = Flask(__name__)

app.secret_key = "dev-secret-change-me"
# == Your Route's Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

## Listings Routes

# GET /listings
# Returns the listings index
@app.route('/listings', methods=['GET'])
def get_all_listings():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listings = listings_repo.all()
    return render_template('listings/index.html', listings=listings)

# GET /listings/<id>
# Returns the listing details page for that listing id
@app.route('/listings/<id>', methods=['GET'])
def get_single_listing(id):
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listing = listings_repo.find(id)
    if listing is None:
        return "Sorry, that listing does not exist.", 404
    else: 
        return render_template('listings/show.html', listing=listing)
    
# GET listings/new
# Returns the new listings page
@app.route('/listings/new', methods=['GET'])
def get_new_listing():
    return render_template('listings/new.html')

    
# POST /listings/new
# Creates listing and redirects to listings/<id> for the new listing
@app.route('/listings/new', methods=['POST'])
def create_listing():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)

    # set the listing params
    owner_id = request.form["owner_id"]
    title = request.form["title"]
    price_per_night = request.form["price_per_night"]
    county = request.form["county"]
    listing_description = request.form["listing_description"]
    img_url = request.form["img_url"]

    # create the listing object and pass into #create method 
    listing = Listing(None, owner_id, title, price_per_night, county, listing_description, img_url)
    listings_repo.create(listing)

    return redirect(f"/listings/{listing.id}")








## Login route including validation steps

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return "Missing username or password", 400
    
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT id FROM users WHERE email = %s AND password_hash = %s", [email, password])

    if len(rows) > 0:
        user_id = rows[0]["id"]
        session["user_id"] = user_id
        return render_template("test_listings.html"), 200
    else:
        return "Error: Invalid username or password", 401
    
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect("/login")

@app.route('/hostings', methods=['GET'])
def hostings():
    user_id = session.get("user_id")
    
    if not user_id:
        return redirect("/login")

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)

    hostings = booking_repo.hostings_for_host(user_id)

    return render_template("hostings.html", hostings = hostings), 200


@app.route('/book', methods=['POST'])
def request_a_booking():
    guest_id = request.form['guest_id']
    listing_id = request.form['listing_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    checkout_date = request.form['checkout_date']
    booking_price = request.form['booking_price']

#Add validation here - e.g. User inputs past date

    booking = Bookings (
        None,
        'Requested',
        guest_id,
        listing_id,
        start_date,
        end_date,
        checkout_date,
        booking_price,
    )

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.create(booking)

    return "Your booking request has been submitted successfully.", 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))