from lib.Bookings import *
from lib.database_connection import *
from lib.Listings import *

class BookingRepository():

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()

    def find_booking_by_listing(self, listing_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE listing_id = %s', [listing_id])
        
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['listing_id'], row['requester_id'], row['start_date'], row['end_date'], row['status'])

            bookings.append(item)

        return bookings
    
    def find_booking_by_requester_id(self, requester_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE requester_id = %s', [requester_id])
        
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['listing_id'], row['requester_id'], row['start_date'], row['end_date'], row['status'])
            bookings.append(item)

        return bookings
    
    def find_booking_by_listing_user(self, user_id):
        rows = self._connection.execute('SELECT listings.id AS listings_id, listings.name, listings.description, listings.location, listings.price, listings.user_id, bookings.id AS bookings_id, bookings.listing_id, bookings.requester_id, bookings.start_date, bookings.end_date, bookings.status FROM bookings JOIN listings ON bookings.listing_id = listings.id WHERE listings.user_id = %s', [user_id])

        bookings = []
        for row in rows:
            item = Booking(row['bookings_id'], row['listing_id'], row['requester_id'], row['start_date'], row['end_date'], row['status'])
            bookings.append(item)

        return Listing(rows[0]['listings_id'], rows[0]['name'], rows[0]['description'], rows[0]['location'], rows[0]['price'], rows[0]['user_id'], bookings)
        

    
    def is_listing_available(self, listing_id, start_date, end_date):
        rows = self._connection.execute('SELECT * FROM bookings WHERE listing_id = %s AND start_date <= %s AND end_date >= %s AND status = "confirmed"', [listing_id, start_date, end_date])
        
        if len(rows) > 0:
            return False
        return True
    

    def create_booking(self, requester_id, listing_id, start_date, end_date):
        if self.is_listing_available(listing_id, start_date, end_date):
            self._connection.execute('INSERT INTO Bookings (listing_id, requester_id, start_date, end_date, status) VALUES ( %s, %s, %s, %s, "requested")', [listing_id, requester_id, start_date, end_date])
            return "Booking submitted successfully"
        return "There was an error submitting your booking. Try again later."