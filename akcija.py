n = int(input())
prices = []
for _ in range(n):
    price = int(input())
    prices.append(price)
prices_sorted = sorted(prices, reverse=True)
chunks = [prices_sorted[x : x + 3] for x in range(0, n, 3)]
min_price = 0
for chunk in chunks:
    if len(chunk) >= 3:
        chunk.pop()
    while chunk:
        min_price += chunk.pop()
print(min_price)
