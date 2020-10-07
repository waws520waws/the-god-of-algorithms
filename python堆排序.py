
# 使用python自带的函数heapq完成堆排序

import heapq
import random

li = list(range(100))
random.shuffle(li)
print(li)

heapq.heapify(li)  # 建堆(小根堆)
print(li)

n = len(li)
for i in range(n):
    print(heapq.heappop(li),end=",")