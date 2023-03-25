
# 2. Implement a head recursive function to find the maximum element in the list.
# Maximum number in list

def find_Maximum(num):
    maximum=num[0]
    for i in range(1,len(num)):
        if num[i]>maximum:
            maximum=num[i]
    return maximum
print(find_Maximum([34,56,23,45,78,21,13]))






