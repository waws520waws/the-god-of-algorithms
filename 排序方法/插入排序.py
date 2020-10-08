def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tem = li[i]
        while j >= 0 and tem < li[j]:
            li[j + 1] = li[j]
            j = j - 1
        li[j+1]=tem
        print(li)
    return li


a = [7,3,1,3,2,4,2,5,6]
print(a)
print(insert_sort(a))
