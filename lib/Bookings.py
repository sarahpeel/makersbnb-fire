class Booking():

    def __init__(self, id, listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price):
        self.id = id
        self.listing_id = listing_id
        self.requester_id = requester_id
        self.requester_name = requester_name #added
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.listing_name = listing_name #added
        self.price = price #added

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Booking({self.id}, {self.listing_id}, {self.requester_id}, {self.requester_name}, {self.start_date}, {self.end_date}, {self.status},{self.listing_name}, {self.price})'
        