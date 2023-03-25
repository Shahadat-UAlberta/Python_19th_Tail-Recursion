def find_Maximum(num):
    maximum=num[0]
    for start in range(1,len(num)):
        if num[start]>maximum:
            maximum=num[start]
    return maximum
print(find_Maximum([34,56,23,45,78,21,13]))
