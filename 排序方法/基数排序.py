def radix_sort(li):
    max_num = max(li)
    it = 0
    # it能得到数值几位，决定几次循环
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            # 取出各个数位上的数字，用于分桶
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1
    return li

import random
li = [random.randint(0,1000) for _ in range(1000)]
print(radix_sort(li))

