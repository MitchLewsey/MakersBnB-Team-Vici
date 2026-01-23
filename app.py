import os
from datetime import date, datetime
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.listing_repository import *
from lib.BookingRepository import *
from lib.bookings import *
from lib.user_repository import *


# Create a new Flask app
app = Flask(__name__)

@app.context_processor
def inject_user():
    return {
        "user_name": session.get("user_name"),
        "user_id": session.get("user_id")
    }

app.secret_key = "dev-secret-change-me"

def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()
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
    if "user_id" not in session:
        return redirect("/login")
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listings = listings_repo.all()
    return render_template('listings/index.html', listings=listings)

# GET /listings/<id>
# Returns the listing details page for that listing id
@app.route('/listings/<id>', methods=['GET'])
def get_single_listing(id):
    if "user_id" not in session:
        return redirect("/login")
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listing = listings_repo.find(id)
    if listing is None:
        return render_template('listings/error.html', listing=listing), 404        
        # return "Sorry, that listing does not exist.", 404
    else: 
        return render_template('listings/show.html', listing=listing)
    
# GET listings/new
# Returns the new listings page
@app.route('/listings/new', methods=['GET'])
def get_new_listing():
    if "user_id" not in session:
        return redirect("/login")
    return render_template('listings/new.html')

    
# POST /listings/new
# Creates listing and redirects to listings/<id> for the new listing
@app.route('/listings/new', methods=['POST'])
def create_listing():

    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)

    owner_id = session["user_id"]
    title = request.form["title"]
    price_per_night = request.form["price_per_night"]
    county = request.form["county"]
    listing_description = request.form["listing_description"]
    img_url = request.form["img_url"]

    listing = Listing(None, owner_id, title, price_per_night, county, listing_description, img_url)
    listings_repo.create(listing)

    return redirect(f"/listings/{listing.id}")

## Sign up and Login route including validation steps

@app.route("/signup", methods=["GET"])
def signup_page():
    if session.get("user_id"):
        return redirect("/listings")
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if not name or not email or not password:
        return "Missing fields", 400

    if user_repo.find_by_email(email):
        return "Email already exists", 400

    user = User(None, name, email, password)
    user = user_repo.create(user)

    session.clear()
    session["user_id"] = user.id
    session["user_name"] = user.name

    return redirect("/listings")

@app.route('/login', methods=['GET'])
def login_page():
    if session.get("user_id"):
        return redirect("/listings")
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return "Missing username or password", 400
    
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT id, name FROM users WHERE email = %s AND password_hash = %s", [email, password])

    if len(rows) > 0:
        user_id = rows[0]["id"]
        user_name = rows[0]["name"]
        session["user_id"] = user_id
        session["user_name"] = user_name
        return redirect("/listings")
    else:
        return "Error: Invalid username or password", 401
    
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect("/login")

# GET page for all your listings that you own
@app.route('/hostings', methods=['GET'])
def hostings():
    user_id = session.get("user_id")
    
    if not user_id:
        return redirect("/login")

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)

    hostings = booking_repo.hostings_for_host(user_id)

    return render_template("hostings.html", hostings = hostings), 200

# checkout routes
@app.route("/listings/<int:listing_id>/checkout", methods=["GET"])
def checkout_page(listing_id):
    if "user_id" not in session:
        return redirect("/login")

    connection = get_flask_database_connection(app)
    listing_repo = ListingRepository(connection)

    listing = listing_repo.find(listing_id)
    if listing is None:
        return "Listing not found", 404

    return render_template("checkout.html", listing=listing), 200

##Bookings Routes - shows you all the listings have booked

@app.route('/bookings', methods=['GET'])
def get_all_my_bookings():
    if "user_id" not in session:
        return redirect("/login")

    guest_id = session["user_id"]
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)

    bookings = repository.find_by_guest_id(guest_id)
    return render_template('bookings.html', bookings=bookings), 200


@app.route('/bookings', methods=['POST'])
def request_a_booking():
    if "user_id" not in session:
        return redirect("/login")
    
    guest_id = session["user_id"]

    listing_id = request.form['listing_id']
    start_date_str = request.form['start_date']
    end_date_str = request.form['end_date']

    if not listing_id or not start_date_str or not end_date_str:
        return "Missing fields", 400
    
    start_date = _parse_date(start_date_str)
    end_date = _parse_date(end_date_str)
    if end_date <= start_date:
        return "End date must be after start date", 400
    if start_date < date.today():
        return "Start date cannot be in the past", 400
    
    checkout_date = date.today()

    connection = get_flask_database_connection(app)

    listing_repo = ListingRepository(connection)
    listing = listing_repo.find(int(listing_id))

    if listing is None:
        return "Listing not found", 404

    nights = (end_date - start_date).days
    price_per_night = float(listing.price_per_night)
    booking_price = round(price_per_night * nights, 2)

    booking = Bookings (
        None,
        'Requested',
        guest_id,
        int(listing_id),
        start_date,
        end_date,
        checkout_date,
        booking_price,
    )

    booking_repo = BookingRepository(connection)
    booking = booking_repo.create(booking)

    return redirect(f"/bookings/{booking.id}/confirmation")
    
@app.route("/bookings/<int:booking_id>/confirmation")
def booking_confirmation(booking_id):
    if "user_id" not in session:
        return redirect("/login")

    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)

    booking = repo.find_receipt(booking_id) 
    return render_template("booking_confirmation.html", booking=booking), 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))