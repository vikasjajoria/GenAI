# --------------factorial--------------
def factorial(n):

    # -------edge cases-----------
    if n == 0 or n == 1:
        return 1

    # -----------negative case----------------
    elif  n < 0:
        print("Error: Factorial is not define of negative number")
        return None

    # --------------recursive case-------------------
    else:
        return  n * factorial(n-1)


# ------test case---
print(factorial(5))
print(factorial(0))
print(factorial(-3))

    

