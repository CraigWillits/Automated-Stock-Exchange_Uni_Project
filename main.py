from account import Account
from bidding import Bidding
from asking import Asking


class MainMenu:
    def __init__(self):
        self.accounts = []
        self.bidding = []
        self.asking = []
        self.next_user_id = 1


    def run(self):
        while True:
            print('1. Create Account')
            print('2. Log In')
            print('3. Make a Stock Bidding')
            print('4. Make a Stock Asking')
            print('5. Exit Program')
            menu_location = int(input('Enter Number to Continue: '))

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
        print('=== Create New Account ===\n')
        f_name = input('Plese Enter Your First Name: ')
        l_name = input('Plese Enter Your Last Name: ')
        email = input('Plese Enter Your Email: ')

        new_account = Account(f_name, l_name, email, self.next_user_id)
        self.accounts.append(new_account)
        print(f"\nAccount created successfully! Your User ID is: {self.next_user_id}")

        self.next_user_id += 1

        
    def log_into_account(self):
        print('=== Log into Account ===\n')
        user_id = input('Please Enter Your User ID: ')
        self.user_id = user_id

    def make_stock_bid(self):
        pass

    def make_stock_ask(self):
        pass

    def exit_program(self):
        print("\nThank you for using the Automated Stock Exchange System. Goodbye!")
        exit()

    def check_for_matches(self):
        pass


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()