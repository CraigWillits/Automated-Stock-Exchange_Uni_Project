# Test Scenarios for Professor / TA

**How to Test the Automated Stock Exchange System**

1. Run the program: `python main.py`
2. Create at least **one account** (option 1) and use another already implemented account; write down their User IDs also.
3. Use the test scenarios below.  
   - **BUYER_ID** = User ID placing the bid (option 3)  
   - **SELLER_ID** = User ID placing the ask (option 4)

After each test, check:
- The success message printed on screen
- `transactions.txt` for the new transaction line
- `biddings.json` and `askings.json` for correct updates

---

### Scenario 1: Full Match (Equal Amounts)

1. Option 3 (Bid): Stock = AAPL, Price = 150, Amount = 10, User = BUYER_ID
2. Option 4 (Ask): Stock = AAPL, Price = 150, Amount = 10, User = SELLER_ID

**Expected Result:**
- Message: `10 order(s) successfully has been executed at 150.0`
- Both bid and ask are completely removed
- `transactions.txt` contains: `AAPL,10,150.0,BUYER_ID,SELLER_ID`

---

### Scenario 2: Partial Match (Asking Amount > Bidding Amount)

1. Option 4 (Ask): Stock = MSFT, Price = 300, Amount = 20, User = SELLER_ID
2. Option 3 (Bid): Stock = MSFT, Price = 310, Amount = 8, User = BUYER_ID

**Expected Result:**
- Message: `8 order(s) successfully has been executed at 310.0`
- Bid is removed
- Ask remains with amount reduced to 12
- `transactions.txt` contains: `MSFT,8,310.0,BUYER_ID,SELLER_ID`

---

### Scenario 3: Partial Match (Bidding Amount > Asking Amount)

1. Option 3 (Bid): Stock = TSLA, Price = 250, Amount = 30, User = BUYER_ID
2. Option 4 (Ask): Stock = TSLA, Price = 240, Amount = 12, User = SELLER_ID

**Expected Result:**
- Message: `12 order(s) successfully has been executed at 250.0`
- Ask is removed
- Bid remains with amount reduced to 18
- `transactions.txt` contains: `TSLA,12,250.0,BUYER_ID,SELLER_ID`

---

### Scenario 4: No Match

1. Option 3 (Bid): Stock = GOOG, Price = 100, Amount = 5, User = BUYER_ID
2. Option 4 (Ask): Stock = GOOG, Price = 150, Amount = 5, User = SELLER_ID

**Expected Result:**
- No execution message
- No new line in `transactions.txt`
- Both bid and ask remain unchanged

---

**Reset Instructions (if needed):**
Delete `accounts.json`, `biddings.json`, `askings.json`, and `transactions.txt` to start fresh.

**Note:** The program automatically saves all data. You can log in with the same User ID on future runs.