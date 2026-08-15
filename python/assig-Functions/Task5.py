# -------filter()-----------
prices = [100,250,400,1200,50,2000,850]

# ----greater------
greater_than_500 = list(filter(lambda price: price > 500, prices))

# -----less then or equal -------
less_then_or_equal_500 = list(filter(lambda price: price <= 500, prices))


print("Prices greater than 500:", greater_than_500)
print("Prices less then or qual 500 :", less_then_or_equal_500)
