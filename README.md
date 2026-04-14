# Automated Stock Exchange System

This is the INSY 3300 group project: an automated stock exchange system built entirely in Python.

## Project Requirements (as stated in Project.docx)

The system includes:
- A main menu with four options:
  1. Create an account
  2. Make a Stock bidding
  3. Make a Stock Asking
  4. Exit the program

- **Account class** – stores first name, last name, email address, and automatically assigns a unique user ID.
- **Bidding class** – stores stock name, bidding price, amount, and user ID.
- **Asking class** – stores stock name, asking price, amount, and user ID.

- After every bidding or asking is created, the program automatically checks for matches:
  - A match occurs when the stock name is the same and bidding price ≥ asking price.
  - When a match is found, the program executes the order and prints:  
    `{Number_of_orders} order(s) successfully has been executed at {bidding_price}`

- Match handling follows the three exact scenarios:
  1. Asking amount equals bidding amount → delete both instances. Number of orders = the amount.
  2. Asking amount > bidding amount → update asking amount (subtract orders), delete bidding instance.
  3. Bidding amount > asking amount → update bidding amount (subtract orders), delete asking instance.

- Every successful match is written to a text file (`transactions.txt`) containing:  
  stock name, number of orders, execution price, bidding user ID, asking user ID.

- A separate report document explains how the system was created, includes screenshots and explanations of different test scenarios, and ends with team member contributions (written by the team leader).

## Folder Structure (for this repository)

```bash
automated-stock-exchange/
├── main.py              # Main program with the menu loop
├── account.py           # Account class
├── bidding.py           # Bidding class
├── asking.py            # Asking class
├── transactions.txt     # Text file the program creates/appends
└── Project-Report.pdf   # Report with explanations, screenshots, and contributions
