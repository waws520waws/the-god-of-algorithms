
def select_sort(li):
    for i in range(len(li)):     #趟数
        min_loc= i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if i != min_loc:
            li[i],li[min_loc] = li[min_loc],li[i]
    return li

a = [7,3,1,3,2,4,2,5,6]
print(select_sort(a))
