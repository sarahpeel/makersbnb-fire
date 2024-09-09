from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection
        self._connection.connect()

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"])
            users.append(item)
        return users

    def create_new_user(self, user):
        self._connection.execute('INSERT INTO users (username) VALUES (%s);', [user.username])
        return None
