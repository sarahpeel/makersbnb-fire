from lib.User import User

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
        username = user.username
        self._connection.execute('INSERT INTO users (username) VALUES (%s);', [username])
        rows = self._connection.execute(
            'SELECT id from users WHERE username = %s', [username])
        row = rows[0]
        return row["id"]
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["username"])
