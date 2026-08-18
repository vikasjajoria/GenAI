prices=[120,350,'abc',500,-200,800] 

total = 0


for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Value is not a number")

        if price < 0:
            raise ValueError("Negative value not allowed") 

        total += price

        print("Runing Total:", total)

    except TypeError as e:
        print("Skipped:", price,"-", e)

    except ValueError as a:
        print('Skipped:', price, "-", a)

print("Final Total:", total)
                  