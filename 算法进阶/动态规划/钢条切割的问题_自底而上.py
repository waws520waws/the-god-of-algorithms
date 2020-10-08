import time

# 自底向上的非递归,我们将f(1)和f(2)计算出来，存储起来，
# 然后计算f(3)的时候，我们使用计算好的f(1)和f(2),直接从存
# 储中拿出来使用，不用重新计算，速度变快了
# 时间复杂度是O(n^2)

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs" % (func.__name__, t2 - t1))
        return result
    return wrapper

# p = [0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rod_dp(p,n):
    r = [0]
    for i in range(1,n+1):
        res = 0
        # 假设这个部分i为4，我们的j就是1，2，3，4，
        # 实际上就是p[1]+r[3],p[2]+r[2],p[3]+r[1],p[4]+r[0]
        # 找到最大的res作为当前长度的最佳价格
        for j in range(1,i+1):
            res = max(res,p[j]+r[i-j])
        r.append(res)
    return r[n]

print(cut_rod_dp(p,9))


