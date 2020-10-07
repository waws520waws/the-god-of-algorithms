# 归并排序
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp
    return li


# def merge_sort(li, low, high):
#     if low < high:  # 至少两个元素,递归
#         mid = (low + high) // 2
#         merge_sort(li, low, mid)
#         merge_sort(li, mid + 1, high)
#         merge(li, low, mid, high)

def merge_sort_test(li, low, high):
    if low < high:  # 至少两个元素,递归
        mid = (low + high) // 2
        merge_sort_test(li, low, mid)
        merge_sort_test(li, mid + 1, high)
        merge(li, low, mid, high)
        print(li[low:high+1])

import random
li = list(range(16))
random.shuffle(li)
print(li)
merge_sort_test(li,0,len(li)-1)
print(li)

"""
原始数据
[11, 13, 5, 14, 8, 1, 3, 2, 4, 12, 7, 6, 15, 0, 9, 10]

最底层分割
[11, 13]
[5, 14]
合并
[5, 11, 13, 14]
最底层分割
[1, 8]
[2, 3]
合并
[1, 2, 3, 8]
合并
[1, 2, 3, 5, 8, 11, 13, 14]
最底层分割
[4, 12]
[6, 7]
合并
[4, 6, 7, 12]
最底层分割
[0, 15]
[9, 10]
合并
[0, 9, 10, 15]
合并
[0, 4, 6, 7, 9, 10, 12, 15]
合并
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
