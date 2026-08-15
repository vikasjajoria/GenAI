# task1) 

# -------------------print the second and last number-------------------
products =["Apple","Shoes","Phone","Book","Laptop","Shirt"]
print(products[1], products[-1])        


#----------------append two products------------------------
products =["Apple","Shoes","Phone","Book","Laptop","Shirt"]

products.append("Mango")
products.append("Car")

print(products)


# --------------tuple-----------------------
simple_product=("laptop",50000,"Electronics")

# convert into a list
convert_to_list = list(simple_product)

# change the price
convert_to_list[1]=40000

# covert back to a tuple 
simple_product= tuple(convert_to_list)

print(simple_product)


