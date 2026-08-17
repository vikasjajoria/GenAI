from shop_package import (
    apply_discount,
    flat_discount,
    calculate_total,
    apply_tax
)


# Test apply_discount()
print("10% Discount:", apply_discount(1000, 10))

# Test flat_discount()
print("Flat Discount:", flat_discount(1000))

# Test calculate_total()
prices = [100, 200, 300, 400]
total = calculate_total(prices)

print("Total Bill:", total)

# Test apply_tax()
final_amount = apply_tax(total)

print("Final Bill with 5% Tax:", final_amount)


# Test all cases
print("\n--- Testing All Cases ---")

print(apply_discount(500, 10))
print(apply_discount(1000, 20))
print(apply_discount(200, 0))

print(flat_discount(500))
print(flat_discount(100))
print(flat_discount(50))

print(calculate_total([100, 200, 300]))
print(calculate_total([500]))
print(calculate_total([]))

print(apply_tax(100))
print(apply_tax(500))
print(apply_tax(0))