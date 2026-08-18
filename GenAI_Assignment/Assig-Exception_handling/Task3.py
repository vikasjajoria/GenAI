def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 to 120")

try:
    age= int(input("Enter your age..."))
    check_age(age)
    print("Valid Age:", age)

except ValueError as e:
    print("Custom Error:", e)    

    