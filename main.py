import random
import json
import os
from account import Account
from bidding import Bidding
from asking import Asking


class MainMenu:
    def __init__(self):
        self.accounts = []
        self.bidding = []
        self.asking = []
        self.current_user_id = None
        self.load_data()

    def load_data(self):
        '''Load All Saved Data'''
        if os.path.exists('accounts.json'):
            with open('accounts.json', 'r') as f:
                data = json.load(f)
                self.accounts = [Account.from_dict(acc) for acc in data]
            #print(f'[DEBUG] Loaded {len(self.accounts)} account(s)')

        if os.path.exists('biddings.json'):
            with open('biddings.json', 'r') as f:
                data = json.load(f)
                self.bidding = [Bidding.from_dict(b) for b in data]

        if os.path.exists('askings.json'):
            with open('askings.json', 'r') as f:
                data = json.load(f)
                self.asking = [Asking.from_dict(a) for a in data]

    def save_data(self):
        '''Save All Data'''
        with open('accounts.json', 'w') as f:
            json.dump([acc.to_dict() for acc in self.accounts], f, indent=2)

        with open('biddings.json', 'w') as f:
            json.dump([b.to_dict() for b in self.bidding], f, indent=2)

        with open('askings.json', 'w') as f:
            json.dump([a.to_dict() for a in self.asking], f, indent=2)



    def run(self):
        while True:
            print('\n=== Automated Stock Exchange System ===')
            print('1. Create Account')
            print('2. Log In')
            print('3. Make a Stock Bidding')
            print('4. Make a Stock Asking')
            print('5. Exit Program')
            try:
                menu_location = int(input('\nEnter Number to Continue: '))
            except ValueError:
                print('Please enter a number.')
                continue

            if menu_location == 1:
                self.account_creation()
            elif menu_location == 2:
                self.log_into_account()
            elif menu_location == 3:
                self.make_stock_bid()
            elif menu_location == 4:
                self.make_stock_ask()
            elif menu_location == 5:
                self.exit_program()
            else:
                print('Invalid choice. Please try again.')


    def account_creation(self):
        print('\n=== Create New Account ===')
        f_name = input('\nEnter Your First Name: \n')
        l_name = input('\nEnter Your Last Name: \n')
        email = input('\nEnter Your Email: \n')

        while True:
            user_id = random.randint(100000, 999999)
            if not any(acc.get_user_id() == user_id for acc in self.accounts):
                break

        new_account = Account(f_name, l_name, email, user_id)
        self.accounts.append(new_account)
        self.save_data()

        print(f'\nAccount created successfully!')
        print(f'\nYour unique User ID is: {user_id}\n')
        print('Save this ID — it is the ONLY way to access your account.')


    def log_into_account(self):
        print('\n=== Log into Account ===\n')
        try:
            entered_id = int(input('Please Enter Your User ID: '))
        except ValueError:
            print("Invalid User ID format.")
            return

        for acc in self.accounts:
            if acc.get_user_id() == entered_id:
                self.current_user_id = entered_id
                print(f'\nLogin successful! Welcome, {acc.first_name} {acc.last_name}')
                print(f'Account: {acc}')
                return

        print('No account found with that User ID.')

    def make_stock_bid(self):
        print('\n=== Make a Stock Bidding ===')
        stock_name = input('Enter Stock Name: ').strip().upper()

        try:
            bidding_price = float(input('Enter Bidding Price: '))
            amount = int(input('Enter Amount: '))
        except ValueError:
            print("Invalid price or amount.")
            return

        if self.current_user_id is not None:
            print(f"You are currently logged in as User ID: {self.current_user_id}")
            use_current = input("Use this logged-in User ID? (y/n): ").strip().lower()
            if use_current == 'y' or use_current == 'yes':
                user_id = self.current_user_id
            else:
                user_id = int(input('Enter User ID for this bid: '))
        else:
            user_id = int(input('Enter Your User ID: '))

        new_bid = Bidding(stock_name, bidding_price, amount, user_id)
        self.bidding.append(new_bid)
        print(f'\nBid placed for {stock_name} at {bidding_price}.')

        self.check_for_matches()
        self.save_data()

    def make_stock_ask(self):
        print('\n=== Make a Stock Asking ===')
        stock_name = input('Enter Stock Name: ').strip().upper()

        try:
            asking_price = float(input('Enter Asking Price: '))
            amount = int(input('Enter Amount: '))
        except ValueError:
            print("Invalid price or amount.")
            return

        if self.current_user_id is not None:
            print(f"You are currently logged in as User ID: {self.current_user_id}")
            use_current = input("Use this logged-in User ID? (y/n): ").strip().lower()
            if use_current == 'y' or use_current == 'yes':
                user_id = self.current_user_id
            else:
                user_id = int(input('Enter User ID for this ask: '))
        else:
            user_id = int(input('Enter Your User ID: '))

        new_ask = Asking(stock_name, asking_price, amount, user_id)
        self.asking.append(new_ask)
        print(f'\nAsk placed for {stock_name} at {asking_price}.')

        self.check_for_matches()
        self.save_data()

    def exit_program(self):
        self.save_data()
        print("\nThank you for using the Automated Stock Exchange System. Goodbye!")
        exit()

    def check_for_matches(self):
        matched = True
        while matched:
            matched = False
            for bid in list(self.bidding):
                for ask in list(self.asking):
                    if bid.stock_name == ask.stock_name and bid.bidding_price >= ask.asking_price:
                        if ask.amount == bid.amount:
                            number_of_orders = bid.amount
                            self.bidding.remove(bid)
                            self.asking.remove(ask)
                        elif ask.amount > bid.amount:
                            number_of_orders = bid.amount
                            ask.amount -= bid.amount
                            self.bidding.remove(bid)
                        else:
                            number_of_orders = ask.amount
                            bid.amount -= ask.amount
                            self.asking.remove(ask)

                        print(f'{number_of_orders} order(s) successfully has been executed at {bid.bidding_price}')
                        self.record_transaction(bid.stock_name, number_of_orders, bid.bidding_price, bid.get_user_id(), ask.get_user_id())
                        self.save_data()
                        matched = True
                        break
                if matched:
                    break

    def record_transaction(self, stock_name, number_of_orders, execution_price, bidding_user_id, asking_user_id):
        with open('transactions.txt', 'a') as f:
            f.write(f'{stock_name},{number_of_orders},{execution_price},{bidding_user_id},{asking_user_id}\n')


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
