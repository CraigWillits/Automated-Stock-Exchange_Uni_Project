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
        if os.path.exists('account.json'):
            with open('accounts.json', 'r') as f:
                data = json.load(f)
                self.accounts = [Account.from_dict(acc) for acc in data]

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
                print("Invalid choice. Please try again.")


    def account_creation(self):
        print('/n=== Create New Account ===')
        f_name = input('Plese Enter Your First Name: ')
        l_name = input('Plese Enter Your Last Name: ')
        email = input('Plese Enter Your Email: ')

        while True:
            user_id = random.randint(100000, 999999)
            if not any(acc.user_id == user_id for acc in self.accounts):
                break

        new_account = Account(f_name, l_name, email, user_id)
        self.accounts.append(new_account)
        self.save_data()

        print(f'\nAccount created successfully!')
        print(f'Your unique User ID is: {user_id}')
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
        pass

    def make_stock_ask(self):
        pass

    def exit_program(self):
        self.save_data()
        print("\nThank you for using the Automated Stock Exchange System. Goodbye!")
        exit()

    def check_for_matches(self):
        pass


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()