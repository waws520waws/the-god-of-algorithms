# 升序排列
def bubble_sort_ab(li):
    for i in range(len(li)-1):              # 趟数
        exchange = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return li
    return li



li = [9,8,7,1,2,3,4,5,6]
print(bubble_sort_ab(li))