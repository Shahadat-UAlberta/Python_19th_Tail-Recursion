# (1) WRITE A HEAD-RECURSIVE FUNCTION TO CALCULATE THE EVEN-FACTORIAL OF GIVEN NUMBER ?

def get_even_factorial(n):
    if n == 2:
        return n
    elif n % 2 == 0:
        return n * get_even_factorial(n - 2)
    elif n % 2 == 1:
        return get_even_factorial(n - 1)

print(get_even_factorial(10))

# (1) WRITE A TAIL-RECURSIVE FUNCTION TO CALCULATE THE EVEN-FACTORIAL OF GIVEN NUMBER ?
def get_even_factorial(n, multiply = 1):
    if n == 0 :
        return multiply
    elif n % 2 == 0 :
        return get_even_factorial(n - 2,multiply = n * multiply)
    elif n % 2 == 1 :
        return get_even_factorial(n - 1,multiply = (n - 1) * multiply)

print(get_even_factorial(5))

