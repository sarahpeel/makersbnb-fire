from lib.User import User
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

"""
Test #create_new_user 
to add a new user
return user_id from the create method
"""
def test_create_new_user(db_connection):
    db_connection.seed('seeds/bnb_db.sql')
    user = UserRepository(db_connection)
    new_user = User(None, 'Lucy')
    user_id = user.create_new_user(new_user)
    assert user_id == 4

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/bnb_db.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, "Catherine")
