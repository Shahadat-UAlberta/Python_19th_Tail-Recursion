# 2. Implement a head-recursive and tail-recursive function to find the maximum element in the list.
# Head Recursion
lst = []
num = int(input("ENTER THE NUMBER OF ELEMENTS : "))
for i in range(0, num):
    elements = int(input())
    lst.append(elements)

print(f"THE LIST AS YOU INPUTTED: {lst}")


def head_find_max_num(list2, num):
    if num == 1:
        return num
    return max(list2[num - 1], head_find_max_num(list2, num - 1))


num1 = lst
num2 = len(num1)
print(f"THE MAXIMUM NUMBER OF THE LIST IS {head_find_max_num(num1, num2)}")

# Tail Recursion
lst = []
num = int(input("ENTER THE NUMBER OF ELEMENTS : "))
for i in range(0, num):
    elements = int(input())
    lst.append(elements)

print(f"THE LIST AS YOU INPUTTED: {lst}")

sum = 0


def tail_find_max_num(list2, num):
    global sum

    if num == 1:
        return num
    else:
        sum += num
    return max(list2[num - 1], tail_find_max_num(list2, num - 1))


num1 = lst
num2 = len(num1)
print(f"THE MAXIMUM NUMBER OF THE LIST IS {tail_find_max_num(num1, num2)}")
