Implement make_stock_bid(self) method
=====================================
**Task:** Create the `make_stock_bid` method inside the `MainMenu` class.

**Exact Requirements from Project.docx:**
- This method runs when the user selects option 2 ("Make a Stock bidding") from the main menu.
- Ask the user to input:
  - Stock name (example: AAPL)
  - Bidding price
  - Amount (number of shares)
  - User ID (the account ID of the person making the bid)
- Create a new `Bidding` object using those 4 values.
- Add the new Bidding object to `self.bidding` list.
- Immediately call `self.check_for_matches()` after the bid is added.
- Print a clear confirmation message that the bid was placed successfully.
- The program should then automatically return to the main menu.

**Optional but recommended:**
- If the user is already logged in (`self.current_user_id` is not None), you can automatically use that User ID instead of asking again.
- Call `self.save_data()` so the bid is saved to the JSON file.

**Deadline:** Please complete this method and push your changes to a branch, then create a Pull Request.



Implement make_stock_ask(self) method
=====================================
**Task:** Create the `make_stock_ask` method inside the `MainMenu` class.

**Exact Requirements from Project.docx:**
- This method runs when the user selects option 3 ("Make a Stock Asking") from the main menu.
- Ask the user to input:
  - Stock name (example: AAPL)
  - Asking price
  - Amount (number of shares)
  - User ID (the account ID of the person making the ask)
- Create a new `Asking` object using those 4 values.
- Add the new Asking object to `self.asking` list.
- Immediately call `self.check_for_matches()` after the ask is added.
- Print a clear confirmation message that the ask was placed successfully.
- The program should then automatically return to the main menu.

**Optional but recommended:**
- If the user is already logged in (`self.current_user_id` is not None), you can automatically use that User ID instead of asking again.
- Call `self.save_data()` so the ask is saved to the JSON file.

**Deadline:** Please complete this method and push your changes to a branch, then create a Pull Request.



Implement check_for_matches(self) and record_transaction(self) methods
======================================================================
**Task:** Create TWO methods in the `MainMenu` class:
1. `check_for_matches(self)`
2. `record_transaction(self, stock_name, number_of_orders, execution_price, bidding_user_id, asking_user_id)`

**Exact Requirements from Project.docx for `check_for_matches`:**
- This method must run automatically after **every** bid or ask is created.
- Loop through the `self.bidding` and `self.asking` lists.
- Look for any pair where:
  - The stock name is exactly the same, AND
  - bidding_price ≥ asking_price
- When a match is found, handle **exactly** one of the 3 scenarios described in the project document:
  1. If asking amount == bidding amount → delete both objects
  2. If asking amount > bidding amount → subtract from asking amount, delete the bidding object
  3. If bidding amount > asking amount → subtract from bidding amount, delete the asking object
- For every successful match, print the **exact** message:
  `{Number_of_orders} order(s) successfully has been executed at {bidding_price}`
- Call `record_transaction` to save the match to `transactions.txt`
- Call `self.save_data()` to persist the updated lists.

**Requirements for `record_transaction`:**
- Open (or create) the file `transactions.txt` in append mode ('a')
- Write one line in this exact format:
  `stock_name,number_of_orders,execution_price,bidding_user_id,asking_user_id`
- You may add a small debug print if you want.

**This is the most important method in the entire project.**



Create TEST_SCENARIOS.md for Professor / TA testing
===================================================
**Task:** Create a new file called `TEST_SCENARIOS.md` in the root of the repository.

**Content to include:**
- Clear step-by-step instructions for the professor/TA on how to test the program.
- At least 4 specific test scenarios:
  1. Full match (equal amounts)
  2. Partial match (asking amount > bidding amount)
  3. Partial match (bidding amount > asking amount)
  4. No match case

Include:
- What the user should do (create accounts, place bids/asks)
- What should happen after each test
- What to check in `transactions.txt`

This file will be used in our final report and for grading.
