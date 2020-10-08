def select_sort(li):
    li_new = []
    for i in range(len(li)):
        min_li = min(li)
        li_new.append(min_li)
        li.remove(min_li)
    return li_new

"""
存在着两个大的缺点：
1.新创建了一个list的大小和原始数据一边大小，若原始数据2G,那新创建的也会是2G,怕内存吃不消
2.时间复杂度远远大于O(n)，因为min和remove都不是O(1)的基本操做。
"""


a = [7,3,1,3,2,4,2,5,6]
print(select_sort(a))