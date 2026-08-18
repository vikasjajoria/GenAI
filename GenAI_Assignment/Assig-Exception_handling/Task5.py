cart = []

class NegativePriceError(Exception):
    pass

while True:
    price_input=input("Enter prices..(or 'q' to quit)")

    if price_input.lower()== 'q':
        break

    try:
        price= float(price_input)

        if price < 0:
            raise NegativePriceError("Negative value not allowed")

        cart.append(price)
        print("Price added:", price)

    except ValueError:
        print("Error: Please enter a valid number")

    except NegativePriceError as e:
        print("Custom Error", e)


print("\nTotal items:", len(cart))
print("Total bill:", sum(cart))                