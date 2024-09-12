class Listing:

#============ Removed occupied and availability. Possibly for sprint 2==========#

    def __init__(self, id, name, description, location, price, user_id, bookings= []):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.price = price
        self.user_id = user_id
        self.bookings = bookings

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Listing({self.id}, {self.name}, {self.description}, {self.location}, {self.price}, {self.user_id}, {self.bookings})'
    
        
