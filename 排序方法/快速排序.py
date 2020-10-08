def partation(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        print(li, " right")
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
        print(li, " left")
    li[left] = temp
    return left

def quick_sort(li,left,right):
    if left < right:
        mid = partation(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid + 1,right)
    return li

a = [5, 2, 7, 3, 4, 6, 8, 7, 1, 2]
print(quick_sort(a, 0, len(a) - 1))
