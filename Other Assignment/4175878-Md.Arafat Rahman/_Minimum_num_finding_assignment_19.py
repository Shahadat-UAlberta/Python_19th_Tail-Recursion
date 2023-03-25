def find_Minimum(num):
    minimum=num[0]
    for start in range(1,len(num)):
        if num[start]<minimum:
            minimum=num[start]
    return minimum
print(find_Minimum([34,56,23,45,78,21,13]))
