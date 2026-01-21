from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"], row["password_hash"])
            users.append(item)
        return users
    
    def get_user(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        if not rows:
            return None
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["password_hash"])
    
    def get_user_password_hash(self, email):
        rows = self._connection.execute('SELECT password_hash FROM users WHERE email = %s', [email])
        if not rows:
            return None
        return rows[0]['password_hash']
        
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)', [user.name, user.email, user.password_hash])
        return None
    
    def update_user(self, user):
        self._connection.execute(
            'UPDATE users SET name = %s, password_hash = %s WHERE email = %s',
            [user.name, user.password_hash, user.email]
        )
        return None

    def delete_user(self, email):
        self._connection.execute(
            'DELETE FROM users WHERE email = %s', 
            [email]
        )
        return None