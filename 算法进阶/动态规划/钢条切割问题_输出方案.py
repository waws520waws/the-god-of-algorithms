import time
# 输出切割的方案
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs" % (func.__name__, t2 - t1))
        return result
    return wrapper

p = [0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40]
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rod_extend(p,n):
    r = [0]
    s = [0]
    for i in range(1,n+1):
        # 记录价格最优值
        res_r = 0
        res_s = 0   # 价格最大值对应的方案的左边不切割的长度
        for j in range(1,i+1):
            if p[j]+r[i-j]>res_r:
                res_r = p[j]+r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n],s

def cur_rod_solution(p,n):
    r,s = cut_rod_extend(p,n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans

r,s = cut_rod_extend(p,20)
print(s)
print(cur_rod_solution(p,20))



