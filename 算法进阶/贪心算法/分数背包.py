
# 分数背包，东西可以拿走一部分，核心思想：先找单位空间价值最大的东西，逐渐填满背包
goods = [(60,10),(100,20),(120,30)]
goods.sort(key=lambda x:x[0]/x[1],reverse = True)
print(goods)

def fractional_backpack(goods,w):
    m = [0 for _ in range(len(goods))]
    for i,(price,weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w/weight
            w=0
            break
    return m

print(fractional_backpack(goods,50))
