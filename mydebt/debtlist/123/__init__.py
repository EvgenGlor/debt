def final_price(*prices, discount=1, **kwargs):
    low = kwargs.get("price_low", min(prices))
    high = kwargs.get("price_high", max(prices))
    return [price - price * discount / 100 for price in prices if low <= price <= high]


print(final_price(100, 200, 300, 400, 500, discount=5))
print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200))
print(final_price(100, 200, 300, 400, 500, discount=5, price_high=200))
print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200, price_high=350))