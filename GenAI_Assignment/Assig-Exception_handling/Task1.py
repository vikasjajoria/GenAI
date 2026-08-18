try:
    numerator = int(input("Enter Numerator..."))
    denominator = int(input("Enter Denominator..."))

    result = numerator/denominator

except ValueError:
    print("Error: Please enter numbers only")

except ZeroDivisionError:
    print("Error: Deniminator can not be Zero")

else:
    print("Result:", result) 

finally:
    print("Operation Complete")           
