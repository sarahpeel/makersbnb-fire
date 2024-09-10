class Listing:

#============ Removed occupied and availability. Possibly for sprint 2==========#

    def __init__(self, id, name, description, location, price, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.price = price
        self.user_id = user_id
        # self.occupied = False
        # self.availability = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Listing({self.id}, {self.name}, {self.description}, {self.location}, {self.price}, {self.user_id})'
    
    # # Call add_availability before adding to repository
    # def add_availability(self, availability):
    #     self.availability.append(availability)
        
