import os

print("File will be created in:", os.getcwd())

file = open("products.txt", "w")

for i in range(3):
    product = input("Enter product name: ")
    price = input("Enter price: ")

    file.write(product + " | " + price + "\n")

file.close()

# Read and print the file
file = open("products.txt", "r")

for line in file:
    print(line.strip())

file.close()

