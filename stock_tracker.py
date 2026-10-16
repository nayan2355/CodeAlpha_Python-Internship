stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 300}
portfolio = {}
total = 0
n = int(input("How many stocks? "))
for _ in range(n):
    s = input("Enter symbol (AAPL/TSLA/GOOGL/MSFT): ").upper()
    q = int(input(f"Qty for {s}: "))
    portfolio[s] = q
print("\n--- Portfolio ---")
for s,q in portfolio.items():
    val = stock_prices.get(s,0) * q
    total += val
    print(f"{s}: {q} x ${stock_prices.get(s,0)} = ${val}")
print(f"\nTotal Investment: ${total}")
with open("portfolio.txt","w") as f:
    f.write(f"Total: ${total}\n")