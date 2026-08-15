def process_prices(prices):

    # -------------apply 10% discount ---------------
    discounted_prices = list(map(lambda price: price - (price * 0.10), prices))

    #   keep only discounted above 500
    filtered_price = list(filter(lambda price: price > 300, discounted_prices))

    return discounted_prices, filtered_price


# ------test----------
discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

print("Discounted prices:", discounted_prices)
print("Filtered prices:", filtered_prices)
