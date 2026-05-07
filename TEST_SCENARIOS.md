# Test Scenarios

How to test the program. Run `python main.py` and create at least 2 accounts first so you have two different User IDs to use as the buyer and the seller.

In the steps below:
- BUYER_ID = the account placing the bid (option 3)
- SELLER_ID = the account placing the ask (option 4)

After each scenario, check `transactions.txt` for a new line in the format:
`stock_name,number_of_orders,execution_price,bidding_user_id,asking_user_id`


## 1. Full match (equal amounts)

1. Option 3: stock = AAPL, bidding price = 150, amount = 10, user = BUYER_ID
2. Option 4: stock = AAPL, asking price = 150, amount = 10, user = SELLER_ID

Should print: `10 order(s) successfully has been executed at 150.0`

Check:
- biddings.json no longer has the AAPL bid
- askings.json no longer has the AAPL ask
- transactions.txt has: `AAPL,10,150.0,BUYER_ID,SELLER_ID`


## 2. Partial match (asking amount > bidding amount)

1. Option 4: stock = MSFT, asking price = 300, amount = 20, user = SELLER_ID
2. Option 3: stock = MSFT, bidding price = 310, amount = 8, user = BUYER_ID

Should print: `8 order(s) successfully has been executed at 310.0`

Check:
- biddings.json: MSFT bid removed
- askings.json: MSFT ask still there but amount = 12
- transactions.txt: `MSFT,8,310.0,BUYER_ID,SELLER_ID`


## 3. Partial match (bidding amount > asking amount)

1. Option 3: stock = TSLA, bidding price = 250, amount = 30, user = BUYER_ID
2. Option 4: stock = TSLA, asking price = 240, amount = 12, user = SELLER_ID

Should print: `12 order(s) successfully has been executed at 250.0`

Check:
- askings.json: TSLA ask removed
- biddings.json: TSLA bid still there but amount = 18
- transactions.txt: `TSLA,12,250.0,BUYER_ID,SELLER_ID`


## 4. No match

1. Option 3: stock = GOOG, bidding price = 100, amount = 5, user = BUYER_ID
2. Option 4: stock = GOOG, asking price = 150, amount = 5, user = SELLER_ID

Nothing should be executed. Both files keep the bid and the ask. transactions.txt does not change.


## Reset between runs

Delete accounts.json, biddings.json, askings.json, transactions.txt and start over with fresh accounts.
