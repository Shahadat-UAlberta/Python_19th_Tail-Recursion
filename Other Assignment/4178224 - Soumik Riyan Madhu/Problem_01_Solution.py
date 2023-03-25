# 1. Write a head-recursive and tail-recursive function to calculate the factorial of a given number.

# Head Recursion:
def head_recur_fact(num):
    if num == 1:
        return num
    else:
        return num * head_recur_fact(num - 1)


number = int(input("ENTER A NUMBER: "))

if number < 0:
    print("SORRY, FACTORIAL DOES NOT EXIST NEGATIVE NUMBER")
elif number == 0:
    print("THE FACTORIAL OF 0 IS 1")
else:
    print(f"THE FACTORIAL OF {number} IS {head_recur_fact(number)}")

# Tail Recursion:
sum = 0


def tail_recur_fact(num):
    global sum

    if num == 1:
        return num
    else:
        sum += num
        return num * tail_recur_fact(num - 1)


number = int(input("ENTER A NUMBER: "))

if number < 0:
    print("SORRY, FACTORIAL DOES NOT EXIST NEGATIVE NUMBER")
elif number == 0:
    print("THE FACTORIAL OF 0 IS 1")
else:
    print(f"THE FACTORIAL OF {number} IS {tail_recur_fact(number)}")
