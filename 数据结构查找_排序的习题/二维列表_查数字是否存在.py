"""
给定一个m*n的二维列表，查找一个数是否存在，列表的如下特性：
* 每一行的列表都是从左到右已经排好的
* 每一行的第一个数字比上一行最后一个数字都大
"""

# # 第一种方法
# class Solution:
#     def searchMatrix(self,matrix,target):
#         """
#         :param matrix: list[list[int]]
#         :param target: int
#         :return: bool
#         """
#         for line in matrix:
#             # 注意这个in的时间复杂度是O(n)，整体的时间复杂度是O(n^2)
#             if target in line:
#                 return True
#         else:
#             return False


class Solution:
    def searchMatrix(self,matrix,target):
        """
        :param matrix: list[list[int]]
        :param target: int
        :return: bool
        """
        h = len(matrix)
        if h == 0:
            return False  # []
        w = len(matrix[0])
        if w == 0:
            return False
        left = 0
        right = w*h-1
        while left <= right:
            mid = (left+right)//2
            # 对mid的数值转化成二维列表中数值的真是存在
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] >target:
                right = mid-1
            else:
                left = mid+1
        else:
            return False

a = [[1,2,3,4],[5,6,7,8],[9,10,12,14]]
s = Solution()
print(s.searchMatrix(a,13))