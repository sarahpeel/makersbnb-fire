import os
from flask import Flask, request, redirect, session, render_template, flash
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
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    return render_template('index.html', logged_in= logged_in)

@app.route('/login', methods=['GET'])
def get_login():
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    if 'user_id' in session:
        return redirect("/listings")
    return render_template('login.html', logged_in=logged_in)


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
            session['user_id'] = user.id
            return redirect("/loginsuccess")
    errors.append("Username has not been registered")
    errors = ", ".join(errors)
    return render_template('/loginfail.html', errors=errors)

@app.route('/loginsuccess', methods=['GET'])
def get_loginsuccess():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    if 'user_id' not in session:
        return redirect('/login')
    elif 'user_id' in session:
        user_id = session['user_id']
        user = user_repo.find(user_id)
        return render_template('loginsuccess.html', user=user, logged_in = logged_in)

@app.route('/loginfail', methods=['GET'])
def get_loginfail():
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    return render_template('loginfail.html', logged_in = logged_in)

@app.route('/register', methods=['GET'])
def get_register():
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    if 'user_id' in session:
        return redirect("/listings")
    return render_template('register.html', logged_in = logged_in)

@app.route('/registerfail', methods=['GET'])
def get_registerfail():
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    return render_template('registerfail.html', logged_in = logged_in)


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
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
        return redirect('/register')
    elif 'user_id' in session:
        return render_template('register_a_space.html', logged_in = logged_in)


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

    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    
    listings = listings_repo.all()
    return render_template('listings.html', listings=listings, logged_in = logged_in)


@app.route('/my_requests', methods=['GET'])
def get_my_requests():
    logged_in = True
    if 'user_id' not in session:
        logged_in = False
        return redirect('/register')
    elif 'user_id' in session:
        user_id = session['user_id']
        connection = get_flask_database_connection(app)
        repo = BookingRepository(connection)
        outgoing = repo.find_booking_by_requester_id(user_id)

        incoming = []
        _incoming = repo.find_booking_by_listing_user(user_id)
        for entry in _incoming:
            for subentry in entry.bookings:
                if subentry.status == "requested":
                    item = subentry
                    incoming.append(item)

        incoming_responded = []
        _incoming = repo.find_booking_by_listing_user(user_id)
        for entry in _incoming:
            for subentry in entry.bookings:
                if subentry.status != "requested":
                    item = subentry
                    incoming_responded.append(item)
                

    return render_template('my_requests.html', outgoing = outgoing, incoming = incoming, incoming_responded = incoming_responded, logged_in = logged_in)

@app.route('/requests_made', methods=['GET'])
def requests_made_redirect():
    return redirect('/my_requests')

@app.route('/requests_received', methods=['GET'])
def requests_received_redirect():
    return redirect('/my_requests')

@app.route('/listings', methods=['POST'])
def request_a_space():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    listing_repo = ListingRepository(connection)
    user_repo = UserRepository(connection)

    user_id = session['user_id']
    user = user_repo.find(user_id)
    username = user.username

    request_date = request.form['requestdate']

    listing_id = request.form['listing_id']
    listing_name = request.form['listing_name']
    price = request.form['price']

    formatted_date = datetime.strptime(request_date, '%Y-%m-%d')

    booking_repo.create_booking(listing_id, user_id, username, formatted_date, formatted_date, listing_name, price)
    
    #  Redirect to requests page
    return redirect('/listings')

@app.route('/update_booking_status', methods=['POST'])
def post_update_booking_status():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    if 'user_id' not in session:
        return redirect('/register')
    listing_id = request.form['listing_id']
    requester_id = request.form['requester_id']
    action = request.form['action']

    if action == 'Confirm':
        booking_repo.change_status_from_requested_to_confirmed(listing_id, requester_id)
        flash('Booking request accepted successfully!')
    elif action == 'Denied':
        booking_repo.change_status_from_requested_to_denied(listing_id, requester_id)
        flash('Booking request rejected.')
    return redirect('/my_requests')

@app.route('/logout')
def logout():
    # remove the user_id from the session if it's there
    session.pop('user_id', None)

    logged_in = True
    if 'user_id' not in session:
        logged_in = False
    return render_template('logout.html', logged_in = logged_in)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
