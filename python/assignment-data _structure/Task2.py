#----------- Parallel list — same length and order as products-------------
products =["Apple","Shoes","Phone","Book","Laptop","Shirt"]

categories = ["Fruit","Fashion","Electronics","Education","Electronics","Fashion"]

categories_set = set(categories)

print(categories_set)


# ----add a new category -------
categories_set.add("Furniture")
print(categories_set)


#--------- Try adding a category that already exists (duplicate)------
categories_set.add("Electronics")
print(categories_set)

print(len(categories_set))