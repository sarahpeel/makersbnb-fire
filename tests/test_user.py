from lib.user import User

"""
test user constructs with id and username
"""
def test_constructs():
    user = User(1, 'Catherine')
    assert user.id == 1
    assert user.username == 'Catherine'

""" test users with the same details
return as equal
"""
def test_equal():
    user1 = User(1, 'Catherine')
    user2 = User(1, 'Catherine')
    assert user1 == user2

"""
test nice formatting
"""
def test_formatting():
    user = User(1, 'Catherine')
    assert str(user) == "User(1, Catherine)"