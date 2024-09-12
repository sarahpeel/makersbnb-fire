class Booking():

    def __init__(self, id, listing_id, requester_id, start_date, end_date, status):
        self.id = id
        self.listing_id = listing_id
        self.requester_id = requester_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Booking({self.id}, {self.listing_id}, {self.requester_id}, {self.start_date}, {self.end_date}, {self.status})'
        