from lib.Listings import Listing

class ListingRepository:

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()


    def add_listing(self, listing):
        listing.price = int(listing.price)
        if listing.price >= 0:
            self._connection.execute('INSERT INTO listings (name, description, location, price, user_id) VALUES (%s, %s, %s, %s, %s)', [listing.name, listing.description, listing.location, listing.price, listing.user_id])
        else:
            raise Exception("Please enter a valid price")

    def all(self):
        rows = self._connection.execute('SELECT * FROM listings')

        listings = []
        for row in rows:
            item = Listing(row['id'], row['name'], row['description'], row['location'], row['price'], row['user_id'])
            listings.append(item)

        return listings
    
    def find(self, listing_id):
        rows = self._connection.execute('SELECT * FROM listings WHERE id = %s', [listing_id])

        return Listing(rows[0]['id'], rows[0]['name'], rows[0]['description'], rows[0]['location'], rows[0]['price'], rows[0]['user_id'])
        