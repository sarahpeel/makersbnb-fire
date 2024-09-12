import os
from flask import Flask, request, redirect, session, render_template
from lib.database_connection import get_flask_database_connection
from datetime import datetime
from lib.user_repository import UserRepository
from lib.User import User
from lib.Listings import Listing
from lib.ListingsRepository import ListingRepository
from lib.Bookings import Booking
from lib.BookingsRepository import BookingRepository

# Create a new Flask app
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    if 'user_id' in session:
        return redirect("/listings")
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    username = request.form['username']
    errors = []
    if username == None or username == "":
        errors.append("Username can't be blank")
        errors = ", ".join(errors)
        return render_template("loginfail.html", errors = errors)
    users = user_repo.all()
    for user in users:
        if user.username == username:
            print("Successful login")
            session['user_id'] = user.id
            return redirect("/loginsuccess")
    errors.append("Username has not been registered")
    errors = ", ".join(errors)
    return render_template('/loginfail.html', errors=errors)

@app.route('/loginsuccess', methods=['GET'])
def get_loginsuccess():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    if 'user_id' not in session:
        return redirect('/login')
    elif 'user_id' in session:
        user_id = session['user_id']
        user = user_repo.find(user_id)
        return render_template('loginsuccess.html', user=user)

@app.route('/loginfail', methods=['GET'])
def get_loginfail():
    return render_template('loginfail.html')

@app.route('/register', methods=['GET'])
def get_register():
    if 'user_id' in session:
        return redirect("/listings")
    return render_template('register.html')

@app.route('/registerfail', methods=['GET'])
def get_registerfail():
    return render_template('registerfail.html')


@app.route('/register', methods=['POST'])
def post_user():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    username = request.form['username']
    errors = []
    if username == None or username == "":
        errors.append("Username can't be blank")
        errors = ", ".join(errors)
        return render_template("registerfail.html", errors = errors)
    users = user_repo.all()
    for user in users:
        if user.username == username:
            errors.append("Username has already been registered.")
            errors = ", ".join(errors)
            return render_template("registerfail.html", errors = errors)
    user = User(None, username) 
    user_id = user_repo.create_new_user(user)
    return redirect("/login")

@app.route('/register_a_space', methods=['GET'])
def get_a_space():
    connection = get_flask_database_connection(app)
    if 'user_id' not in session:
        return redirect('/register')
    elif 'user_id' in session:
        return render_template('register_a_space.html')


@app.route('/register_a_space', methods=['POST'])
def post_a_space():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    if 'user_id' not in session:
        return redirect('/register')
    elif 'user_id' in session:
        user_id = session['user_id']
        space_name = request.form['name']
        description = request.form['description']
        location = request.form['location']
        price = request.form['price']
        new_listing = Listing(None, space_name, description, location, price, user_id)
        listings_repo.add_listing(new_listing)

        return render_template('listingsuccess.html', listing=new_listing)

@app.route('/listings', methods=['GET'])
def get_listings():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listings = listings_repo.all()
    return render_template('listings.html', listings=listings)


@app.route('/my_requests', methods=['GET'])
def get_my_requests():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)
    listings = listings_repo.all()
    requests = ["This", "is", "a", "placeholder"]
    return render_template('my_requests.html', requests=requests, listings=listings)


@app.route('/listings', methods=['POST'])
def request_a_space():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    listing_repo = ListingRepository(connection)

    user_id = session['user_id']

    request_date = request.form['requestdate']

    listing_id = request.form['listing_id']

    formatted_date = datetime.strptime(request_date, '%Y-%m-%d')

    booking_repo.create_booking(listing_id, user_id, formatted_date, formatted_date)
    
    #  Redirect to requests page
    return redirect('/listings')




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
