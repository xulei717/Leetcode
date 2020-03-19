#!/usr/bin/env python
# coding: utf-8

# -- coding:utf-8 --
# @time : 2020-2-10 16:15
# @author : xulei
# @project: leetcode

# In[ ]:


""" 
标签：困难、分治算法、数组、二分查找、华为 
题目： 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# In[ ]:


# In[3]:


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = sorted(nums1 + nums2)
        nl = len(nums)
        if nl%2 == 0:
            return float(nums[nl//2-1]/2 + nums[nl//2]/2)
        else:
            return float(nums[nl//2])


# In[6]:


nums1 = [1, 2]
nums2 = [3, 4]
s = Solution()
result = s.findMedianSortedArrays(nums1, nums2)
print(result)


# 执行结果：通过
# 执行用时 :100 ms, 在所有 Python3 提交中击败了88.59%的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了49.83%的用户

# In[10]:


a = input()
b = input()
for i in [a, b]:
    if len(i) == 8:
        print(i)
    elif len(i) < 8:
        print(i + '0'*(8-len(i)))
    else:
        for j in range(0, len(i), 8):
            if j+8 < len(i):
                print(i[j:j+8])
            else:
                print(i[j:]+'0'*(8-len(i[j:])))
        


# In[ ]:




