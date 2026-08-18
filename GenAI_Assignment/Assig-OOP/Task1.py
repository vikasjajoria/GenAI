#Basic class and object creation 

class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category

    def get_info(self):
        print("Product Name:", self.name)    
        print("Price:", self.price)    
        print("category:", self.category) 


    def discount_apply(self,percent):
        discount = self.price * percent/100
        discounted_price= self.price - discount
        return discounted_price

# create two objects
product1=Product("Laptop",50000,"Electronics")
product2=Product("Shirt",500,"Clothes")


# call get_ingo()
product1.get_info()
print("Price after 10% discount:", product1.discount_apply(10))

print()


product2.get_info()
print("Price after 17% discount:", product2.discount_apply(17))

print()
