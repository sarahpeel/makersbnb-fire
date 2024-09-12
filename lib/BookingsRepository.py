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

        listings = []

        listing_id_list = []
        for row in rows:
            item = row['listing_id']
            if item not in listing_id_list:
                listing_id_list.append(item)
        print(listing_id_list)
        
        for listing_id in listing_id_list:
            bookings = []
            for row in rows:
                if listing_id == row['listing_id']:
                    item = Booking(row['bookings_id'], row['listing_id'], row['requester_id'], row['start_date'], row['end_date'], row['status'])
                    bookings.append(item)
                print(bookings)

                print(listings)
            single_listing = []
            for row in rows:
                if listing_id == row['listing_id'] and single_listing == []:
                    single_listing.append(Listing(row['listings_id'], row['name'], row['description'], row['location'], row['price'], row['user_id'], bookings))
            
            listings = listings + single_listing
        return listings
    
    def is_listing_available(self, listing_id, start_date, end_date):
        status = "confirmed"
        rows = self._connection.execute('SELECT * FROM bookings WHERE listing_id = %s AND start_date <= %s AND end_date >= %s AND status = %s', [listing_id, start_date, end_date, status])
        
        if len(rows) > 0:
            return False
        return True
    

    def create_booking(self, listing_id, requester_id, start_date, end_date):
        status = "requested"
        if self.is_listing_available(listing_id, start_date, end_date):
            self._connection.execute('INSERT INTO Bookings (listing_id, requester_id, start_date, end_date, status) VALUES ( %s, %s, %s, %s, %s)', [listing_id, requester_id, start_date, end_date, status])
            return "Booking submitted successfully"
        return "There was an error submitting your booking. Try again later."
    

    def change_status_from_requested_to_confirmed(self, listing_id, requester_id):
        status_confirmed = "confirmed"
        status_requested = "requested"
        self._connection.execute('UPDATE bookings SET status = %s WHERE listing_id = %s and requester_id = %s and status = %s', [status_confirmed, listing_id, requester_id, status_requested])

    def change_status_from_requested_to_denied(self, listing_id, requester_id):
        status_denied = "denied"
        status_requested = "requested"
        self._connection.execute('UPDATE bookings SET status = %s WHERE listing_id = %s and requester_id = %s and status = %s', [status_denied, listing_id, requester_id, status_requested])