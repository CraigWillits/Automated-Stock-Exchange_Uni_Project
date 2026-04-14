class Asking:
    def __init__(self, stock_name, asking_price, amount, user_id):
        self.stock_name = stock_name
        self.asking_price = float(asking_price)
        self.amount = int(amount)
        self.user_id = int(user_id)
        