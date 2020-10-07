def bucket_sort(li,n=10,max_num = 100):
    buckets =[[] for _ in range(n)]   # 创建桶
    for val in li:
        i = min(val//(max_num//n),n-1)
        # i表示val这个元素放哪个桶中，我们的桶一共100个，这样编号是0~99，我们的最大值可能是10000，在进行i的计算的时候
        # i= 10000//(10000//100) = 100 超出了桶的编号范围，这样我们，就将他放入到最后一个桶中，min的妙用，巧妙的规避了
        # 10000这个数的桶标号越界的问题，不用进行特殊处理
        buckets[i].append(val)
        # 手动保持桶有序
        for j in range(len(buckets[i])-1,0,-1):
            if buckets[i][j-1]>buckets[i][j]:
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

import random
li = [random.randint(0,100) for i in range(1000)]
li = bucket_sort(li)
print(li)

