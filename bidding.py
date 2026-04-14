class Bidding:
    def __init__(self, stock_name, bidding_price, amount, user_id):
        self.stock_name = stock_name
        self.bidding_price = float(bidding_price)
        self.amount = int(amount)
        self.user_id = int(user_id)