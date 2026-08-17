import shop_package.discount as discount
from shop_package.billing import calculate_total, apply_tax


# Call every function inside the package

print("Discount Price:", discount.apply_discount(1000, 10))

print("Flat Discount:", discount.flat_discount(1000))

print("Total Bill:", calculate_total([100, 200, 300]))

print("Bill with Tax:", apply_tax(600))