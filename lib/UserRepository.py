from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()

    def add_user(self, user):
        self._connection.execute('INSERT INTO users (username) VALUES (%s)', (user.username))
