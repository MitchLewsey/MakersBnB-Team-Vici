import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection

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
    

@app.route('/book', methods=['POST'])
def request_booking():
    listing_id = request.form.get('listing_id')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not listing_id or not start_date or not end_date:
        return "Error: missing or invalid date. Please select a valid date.", 405
    
    connection = get_flask_database_connection(app)

    connection.execute(
        "INSERT INTO bookings (listing_id, start_date, end_date) VALUES (%s, %s, %s)",
        [listing_id, start_date, end_date]
    )

    return "Your booking request has been submitted successfully.", 200














# FYI - KEEP THIS AT THE BOTTOM OF THE CODEBASE
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
