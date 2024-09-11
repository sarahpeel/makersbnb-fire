from lib.Bookings import *

class BookingRepository():

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()

    def find_booking_by_listing(self, listing_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE listing_id = %s', [listing_id])
        
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['listing_id'], row['requester_id'], row['start_date'], row['end_date'], row['status'])
            print(type(item.start_date))
            bookings.append(item)

        return bookings
        
    def is_available(self, booking):
        pass

