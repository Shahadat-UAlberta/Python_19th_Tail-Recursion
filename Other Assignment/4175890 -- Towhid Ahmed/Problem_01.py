
# 1. Write a Tail_recursion fonction to calculate the factorial of a given number.
# Only even number

def tail_recursion(num,mul=1):
    if num==0 or num==1:
        return mul
    elif num%2==0:
        return tail_recursion(num-1,mul=num*mul)
    else:
        return tail_recursion(num-1,mul)

number=int(input("Enter a number for even or odd multiply: "))
print(tail_recursion(number))



#  1. Write a Tail_recursion fonction to calculate the factorial of a given number.
# Only even number

def head_recursion(num):
    if num==1:
        return num
    elif num%2==0:
        return num*head_recursion(num-1)
    else:
        return head_recursion(num-1)
number = int(input("Enter a number for even or odd multiply: "))
print(head_recursion(number))








































