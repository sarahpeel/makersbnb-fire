import os
from flask import Flask, request, redirect, session, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.User import User
from lib.Listings import Listing
from lib.ListingsRepository import ListingRepository

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

@app.route('/register', methods=['GET'])
def get_register():
    return render_template('register.html')

@app.route('/registersuccess', methods=['GET'])
def get_registersuccess():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    if 'user_id' not in session:
        return redirect('/register')
    elif 'user_id' in session:
        user_id = session['user_id']
    user = user_repo.find(user_id)
    return render_template('registersuccess.html', user=user)

@app.route('/register', methods=['POST'])
def post_user():
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    username = request.form['username']
    user = User(None, username) 
    user_id = user_repo.create_new_user(user)
    session['user_id'] = user_id
    return redirect("/registersuccess")

@app.route('/register_a_space', methods=['GET'])
def get_a_space():
    connection = get_flask_database_connection(app)
    return render_template('register_a_space.html')


@app.route('/register_a_space', methods=['POST'])
def post_a_space():
    connection = get_flask_database_connection(app)
    listings_repo = ListingRepository(connection)

    space_name = request.form['name']
    description = request.form['description']
    location = request.form['location']
    price = request.form['price']

    new_listing = Listing(None, space_name, description, location, price)
    listings_repo.add_listing(new_listing)

    return render_template('listingsuccess.html', listing=new_listing)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
