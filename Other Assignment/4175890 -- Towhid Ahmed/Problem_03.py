

# 3. Implement a head-recursive and tail-recursive function to find the minimum element in the list.
# Minimum number in list

def find_minimum(num):
    minimum=num[0]
    for i in range(1,len(num)):
        if num[i]<minimum:
            minimum=num[i]
    return minimum

print(find_minimum([29,54,34,65,78,34,23]))
























