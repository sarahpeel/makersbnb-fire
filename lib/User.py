class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'User({self.id}, {self.username})'
        

    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        return True


    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username can't be blank")
        if len(errors) == 0:
            return None
        else:
            return errors
