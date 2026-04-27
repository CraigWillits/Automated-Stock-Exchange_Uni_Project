class Asking:
    def __init__(self, stock_name, asking_price, amount, user_id):
        self.stock_name = stock_name
        self.asking_price = float(asking_price)
        self.amount = int(amount)
        self.__user_id = int(user_id)

    def get_user_id(self):
        return self.__user_id
    
    def to_dict(self):
        return {
            'stock_name': self.stock_name,
            'asking_price': self.asking_price,
            'amount': self.amount,
            'user_id': self.__user_id
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["stock_name"], data["asking_price"], data["amount"], data["user_id"])
        