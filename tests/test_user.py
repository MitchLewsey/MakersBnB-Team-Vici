from lib.user import User

"""
Constructs with name and parameters
"""

def test_constructs():
    user = User(1, "Test Name", "Test Email", "Test Password_Hash")
    assert User.id == 1
    assert User.name == "Test Name"
    assert User.genre == "Test Genre"

def test_user_format():
    user = User(1, "Test Name", "Test Email", "Test Password_Hash")
    assert str(user) == "User(1, Test Name, Test Email, Test Password_Hash)"