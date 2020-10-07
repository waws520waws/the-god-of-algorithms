# 这里我们使用的是顺序存储list的方式，完成堆排序，实际上是一个二维的过程，我们可以想像成为树结构的调整的过程
def sift(li, low, high):
    """
    此为小根堆的方法
    :param li: 存储树结构的list顺序存储结构
    :param low: 表示根节点元素
    :param high: 表示列表中的最后一个位置
    :return:
    """
    i = low  # 根节点
    j = 2 * i + 1  # 找到上面i的孩子节点
    temp = li[i]  # 将需要调整的值进行缓存
    while j <= high:
        if j + 1 < high and li[j] > li[j + 1]:
            j = j + 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp





def topk(li,k):
    heap = li[0:k]
    # 建堆
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    print(heap)
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)
    return heap
    # 遍历li中剩余元素，因为是小根堆，所以上面元素小的被替换掉，始终保持k个数，而且
    # 一共k个值，然后每次都是将最小值放在最上面，然后被列表中的其他大元素替代，然后在调整，始终保证最小值在最上面，方便替换
    # 因为堆中一共K个值，最后列表遍历完成依旧还是K个值，在进行一次堆排序即可

a = [2,3,1,4,5,3,2,7,5,8]
print(topk(a,3))
