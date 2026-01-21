from lib.user import User

"""
Constructs with name and parameters
"""

def test_constructs():
    user = User(1, "Test Name", "Test Email", "Test Password_Hash")
    assert user.id == 1
    assert user.name == "Test Name"
    assert user.email == "Test Email"
    assert user.password_hash == "Test Password_Hash"

def test_user_format():
    user = User(1, "Test Name", "Test Email", "Test Password_Hash")
    assert str(user) == "User(1, Test Name, Test Email, Test Password_Hash)"