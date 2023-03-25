# sum = 0 # Global Variable
#
# def sum_tail_recursive(num):
#     n = 10 #  Local Variable
#     global sum # Sum - Global Variable
#
#     if num == 0:
#         return sum
#
#     else:
#         sum += num
#         return sum_tail_recursive(num - 1)
#
# print(sum)
# print(sum_tail_recursive(5))
# print(sum)
# # num = 5 [ 1 + 2 + 3 + 4 + 5 ] - return


def is_vowel(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def count_vowel_after_consonant(s):
    count = 0
    for i in range(len(s)-1):
        if not is_vowel(s[i]) and is_vowel(s[i+1]):
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(count_vowel_after_consonant(s))