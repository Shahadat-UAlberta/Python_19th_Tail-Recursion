
# (1) WRITE A HEAD-RECURSIVE FUNCTION TO CALCULATE THE EVEN-FACTORIAL OF GIVEN NUMBER ?

def get_even_factorial(n):
    if n == 2:
        return n
    elif n % 2 == 0:
        return n * get_even_factorial(n - 2)
    elif n % 2 == 1:
        return get_even_factorial(n - 1)

print(get_even_factorial(11))

# (1) WRITE A TAIL-RECURSIVE FUNCTION TO CALCULATE THE EVEN-FACTORIAL OF GIVEN NUMBER ?
def get_even_factorial(n, multiply = 1):
    if n == 0 :
        return multiply
    elif n % 2 == 0 :
        return get_even_factorial(n - 2,multiply = n * multiply)
    elif n % 2 == 1 :
        return get_even_factorial(n - 1,multiply = (n - 1) * multiply)

print(get_even_factorial(10))


# (2) IMPLEMENT A HEAD RECURSIVE FUNCTION TO FIND THE MAXIMUM ELEMENT IN THE LIST.

def max_number(lst):
    if len(lst) == 1:
        return lst[0]
    elif lst[0] < lst[1]:
        lst.pop(0)
        return max_number(lst)
    elif lst[0] > lst[1]:
        lst.pop(1)
        return max_number(lst)
    elif lst[0] == lst[1]:
        lst.pop(0)
        return max_number(lst)

lst = [7,5,101,9,100]
print(max_number(lst))

# (3) IMPLEMENT A HEAD RECURSIVE FUNCTION TO FIND THE MINIMUM ELEMENT IN THE LIST.
def min_number(lst):
    if len(lst) == 1:
        return lst[0]
    elif lst[0] < lst[1]:
        lst.pop(1)
        return min_number(lst)
    elif lst[0] > lst[1]:
        lst.pop(0)
        return min_number(lst)
    elif lst[0] == lst[1]:
        lst.pop(0)
        return min_number(lst)

lst = [7,5,101,9,5,-1]
print(min_number(lst))
