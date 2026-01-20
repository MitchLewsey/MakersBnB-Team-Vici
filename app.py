import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

## Login route

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return "Missing username or password", 400

    rows = "SELECT * FROM users WHERE email = %s AND password_hash = %s"

    if rows:
        return render_template("listings.html"), 200
    else:
        return "Error: Invalid username or password", 401
