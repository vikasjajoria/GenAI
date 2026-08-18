# Constractor and Encapsulation

class Product:

    def __init__(self,name,price,category):
        self.name=name
        self.__price=price
        self.category=category

# getter 
    def get_price(self):
        return self.__price

# setter
    def set_price(self, new_price):
        if new_price > 0:
            print("Price update Successfully")
        else:
            print("price must be greater then 0")



# create object
product1 = Product("Shirt",700,"Clothes")


# show original price
print("Original Price:", product1.get_price())


# modify using setter
product1.set_price(1000)


# display updated price
print("Upadated Price:", product1.get_price())


# Try to set a negative price
product1.set_price(-500)

# Display price
print("Final Price:", product1.get_price())