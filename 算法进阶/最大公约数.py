# 求两个数的最大公约数(欧几里得算法/辗转相除法)
# gcd(a,b) = gcd(b.a mod b)

# 递归求解
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)


# 非递归求解
def gcd2(a,b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(12,16))
print(gcd2(12,16))
