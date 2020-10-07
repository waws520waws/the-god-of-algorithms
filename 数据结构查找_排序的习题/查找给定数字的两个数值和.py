"""
给定一个列表和一个整数，设计相关算法找到两个数的下标，使得两个数之和为给定的整数，保证肯定只有一个结果
* 例如：列表[1,2,5,4]与目标整数3，1+2 = 3，结果为（0，1）
"""

# # 第一种方法
# class Solution:
#     def twoSum(self,nums,target):
#         """
#         :param nums: list[int]
#         :param target: int
#         :return: list[int]
#         """
#         n = len(nums)
#         for i in range(n):
#             for j in range(i):
#                 if nums[i] + nums[j] == target:
#                     return sorted([i,j])

# # 有序的列表
# class Solution:
#     def binary_search(self,li,left,right,val):
#         while left <= right:  # 候选区有值
#             mid = (left + right) // 2
#             if li[mid] == val:
#                 return mid
#             elif li[mid] > val:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1
#
#     def twoSum(self,nums,target):
#         """
#         :param nums: list[int]
#         :param target: int
#         :return: list[int]
#         """
#         for i in range(len(nums)):
#             a = nums[i]
#             b = target - a
#             if b >= a:
#                 j = self.binary_search(nums,i+1,len(nums)-1,b)
#             else:
#                 j = self.binary_search(nums, 0, i-1, b)
#             if j == -1:
#                 continue
#             return sorted([i,j])

# 无序的列表
class Solution:
    def binary_search(self,li,left,right,val):
        while left <= right:  # 候选区有值
            mid = (left + right) // 2
            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def twoSum(self,nums,target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        new_nums = [[num,i] for i,num in enumerate(nums)]
        new_nums.sort(key=lambda x:x[0])
        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums,i+1,len(new_nums)-1,b)
            else:
                j = self.binary_search(new_nums, 0, i-1, b)
            if j == -1:
                continue
            return sorted([new_nums[i][0],new_nums[j][0]])




if __name__ == '__main__':
    a = [1,2,3,4]
    target = 3
    print(Solution().twoSum(a,target))