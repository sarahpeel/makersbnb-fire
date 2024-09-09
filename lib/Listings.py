class Listing:

    def __init__(self, id, name, description, location, price):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.price = price
        self.occupied = False

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Listing({self.id}, {self.name}, {self.description}, {self.location}, {self.price}, {self.occupied}, {self.availability})'
    
    def add_availability(self, availability):
        self.availability = availability
        
