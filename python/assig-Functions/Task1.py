def apply_discount(price, discount_percent=5):

    # -------discount should never exceed 60--------
    if discount_percent > 60:
        discount_percent = 60


    discount = price * discount_percent/100

    final_price = price - discount

    return final_price


# ------------test case----------
print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(1000, 70))