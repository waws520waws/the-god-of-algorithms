import time

# 自顶向下的实现递归
# 这个的理解就是我们想计算f(n) 需要先拆解成 f(n-1)和f(n-2),
# 想计算f(n-1) 需要先拆解成 f(n-2)和f(n-3),以此类推，
# 从n逐渐变化成基数1的过程其实就是自顶而下的递归的方式
# 时间复杂度是O(2^n)
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

# 递归：没有记录子问题的解，所以两次子问题的计算特别慢
def cut_rod_recursion(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res=max(res,cut_rod_recursion(p,i)+cut_rod_recursion(p, n - i))
    return res

# 递归：简化版本(讲一端固定成一个长度，另一端进行切割)
def cut_rod_recursion_2(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, p[i] + cut_rod_recursion(p, n - i))
    return res

print(cut_rod_recursion_2(p, 9))
