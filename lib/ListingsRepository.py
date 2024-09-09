from lib.Listings import Listing

class ListingRepository:

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()

    def add_listing(self, listing):
        self._connection.execute('INSERT INTO listings (name, description, location, price, occupied, availability) VALUES (%s, %s, %s, %s, %s, %s)', (listing.name, listing.description, listing.location, listing.price, listing.occupied, listing.availability))