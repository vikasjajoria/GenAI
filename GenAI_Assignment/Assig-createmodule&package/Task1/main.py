import utils
from utils import square


# Test add()
print("Add:", utils.add(10, 5))

# Test subtract()
print("Subtract:", utils.subtract(10, 5))

# Test square()
print("Square:", square(5))


# Test all cases
print("\nAll Test Cases:")

print(utils.add(10, 20))
print(utils.add(-5, 10))
print(utils.add(0, 0))

print(utils.subtract(20, 10))
print(utils.subtract(5, 10))
print(utils.subtract(0, 5))

print(square(5))
print(square(-5))
print(square(0))