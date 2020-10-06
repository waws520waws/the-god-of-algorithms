# 前提条件是：有序的列表
from time_test import *

@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return -1


a = [1, 2, 3, 4, 4, 6, 9, 13, 15]
val1 = 2
print(binary_search(a, val1))
# val2 = 11
# print(binary_search(a, val2))
