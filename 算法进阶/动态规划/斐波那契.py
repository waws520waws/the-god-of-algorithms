# 递归的方式
def fibnacci(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

def fibnacci_no_rec(n):
    # 假设n=6,[0,1,1,2,3,5,8]
    f = [0,1,1]                        # i =0 [0,1,1,2] i= 1  [0,1,1,2,3] i=2 [0,1,1,2,3,5] i=3 [0,1,1,2,3,5,8]
    for i in range(n-2):
        num = f[-1]+f[-2]
        f.append(num)
    return f[n]


print(fibnacci_no_rec(6))