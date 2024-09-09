from lib.user import User
from lib.user_repository import UserRepository

"""
When I call #all method
Returns list of all users
"""
def test_all_to_return_users(db_connection):
    db_connection.seed('seeds/bnb_db.sql')
    users = UserRepository(db_connection)
    assert users.all() == [
        User(1, 'Catherine'),
        User(2, 'Sarah'),
        User(3, 'Andy')
    ]

"""
Test #create_new_user 
to add a new user
return list of all users including new user
"""
def test_create_new_user(db_connection):
    db_connection.seed('seeds/bnb_db.sql')
    user = UserRepository(db_connection)
    new_user = User(None, 'Lucy')
    user.create_new_user(new_user)
    result = user.all()
    assert result == [
        User(1, 'Catherine'),
        User(2, 'Sarah'),
        User(3, 'Andy'),
        User(4, 'Lucy')
    ]

