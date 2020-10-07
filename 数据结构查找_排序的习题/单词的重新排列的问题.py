"""
1.给定两个字符串s和t,判断t是否是s的重新排列后组成的单词
s = "nangram"  t = "anagram"  return true
s = "cat"  t = "hat"  return false
"""

# # 第一种方法
# class Solution:
#     def isAnagram(self,s,t):
#         ss = list(s)
#         tt = list(t)
#         ss.sort()
#         tt.sort()
#         return ss == tt


# # 第二种方法：一句话搞定
# class Solution:
#     def isAnagram(self,s,t):
#         return sorted(list(s)) == sorted(list(t))

# 第三种方法：字母数量对比
class Solution:
    def isAnagram(self,s,t):
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch,0)+1
        for ch in t:
            dict2[ch] = dict2.get(ch,0)+1
        return dict1 == dict2

s = Solution()
print(s.isAnagram("anagram","naagram"))