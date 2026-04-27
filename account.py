class Account:
    def __init__(self, first_name, last_name, email, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.__user_id = user_id
    
    def get_user_id(self):
        '''Safely Access User Id'''
        return self.__user_id
    
    def to_dict(self):
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'user_id': self.__user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['first_name'], data['last_name'], data['email'], data['user_id'])

    def __str__(self):
        return f'Account {self.get_user_id()}: {self.first_name} {self.last_name} ({self.email})'