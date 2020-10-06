def linearsearch(li,val):
    for i in range(len(li)):
        if li[i] == val:
            return i
    return -1

a = [1,8,2,3,5,6,4,4,2]
val1 = 2
print(linearsearch(a,val1))
val2 = 9
print(linearsearch(a,val2))


"""
2
-1
"""