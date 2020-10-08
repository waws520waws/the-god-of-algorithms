
# 保证时间是按照结束时间排好序的
activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
# 目前已经排好序，假设没有排好序
activities.sort(key=lambda x:x[1])

def activity_selection(a):
    res = [a[0]]
    for i in range(1,len(a)):
        # 一个未选择的活动的开始时间大于活动列表中最后一个的开始时间，证明没有冲突
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res

print(activity_selection(activities))
