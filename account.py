class Account:
    def __init__(self, first_name, last_name, email, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_id = user_id

    def __str__(self):
        return f'Account {self.user_id}: {self.first_name} {self.last_name} ({self.email})'