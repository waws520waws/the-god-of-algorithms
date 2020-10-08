# 这里我们使用的是顺序存储list的方式，完成堆排序，实际上是一个二维的过程，我们可以想像成为树结构的调整的过程
def sift(li, low, high):
    """
    :param li: 存储树结构的list顺序存储结构
    :param low: 表示根节点元素
    :param high: 表示列表中的最后一个位置
    :return:
    """
    i = low  # 根节点
    j = 2 * i + 1  # 找到上面i的孩子节点
    temp = li[i]  # 将需要调整的值进行缓存
    while j <= high:
        if j + 1 < high and li[j] < li[j + 1]:
            j = j + 1  # 左节点小于右节点的话，我们将指针指向右节点
        if li[j] > temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp  # 左右子节点中都没有比temp大的了，就直接将其放在根节点上
            break
    else:
        li[i] = temp  # 我们的j已经越界了，说明i是一个叶子节点，不用在执行调整了，直接放在根节点(实际上就是叶子节点)，即可


def heap_sort(li):
    # 首先先建立堆
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 堆建立完成，进行排序，
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]  # 实现原地存储，不会占用更多的空间资源
        sift(li, 0, i - 1)
    return li

a = [2,3,1,4,5,3,2,7,5,8]
print(heap_sort(a))
