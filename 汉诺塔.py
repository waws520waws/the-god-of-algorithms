# 汉诺塔的问题
# 解决步骤实际上是：
"""
将A上圆盘通过B放置在C的上面
1.首先先将A上的n-1个圆盘经过C放到B上
2.在将A上最大的圆盘移动的C上
3.将B上的n-1个圆盘经过A放置在C上，完成由A--->C的最终的移动
"""


def hannuota(n, a, b, c):
    if n > 0:
        hannuota(n - 1, a, c, b)
        print("please move %s to %s" % (a, c))
        hannuota(n - 1, b, a, c)


hannuota(1, "a", "b", "c")
"""
please move a to c
"""


hannuota(2, "a", "b", "c")
"""
please move a to b
please move a to c
please move b to c
"""

hannuota(3, "a", "b", "c")
"""
please move a to c
please move a to b
please move c to b
please move a to c
please move b to a
please move b to c
please move a to c
"""

hannuota(4, "a", "b", "c")
"""
please move a to b
please move a to c
please move b to c
please move a to b
please move c to a
please move c to b
please move a to b
please move a to c
please move b to c
please move b to a
please move c to a
please move b to c
please move a to b
please move a to c
please move b to c
"""
