#!/usr/bin/env python
# coding: utf-8

# # -*- coding:utf-8 -*-
# # @time   : 2020-2-10 15:27
# # @author : xulei
# # @project: leetcode

# """
# 标签：简单、哈希表、数组、华为
# 题目：
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# """

# In[ ]:



# In[13]:


class Solution:
    def twoSum(self, nums, target):
        nsl = sorted(nums)
        for i in range(len(nsl)):
            t = target - nsl[i]
            if t in nsl[i+1:]:
                index1 = nums.index(nsl[i])
                index2 = nums.index(t)
                if index1 == index2:
                    index2 = nums[index1+1:].index(t) + index1 + 1
                return [index1, index2]
        


# 执行结果：通过
# 执行用时 :52 ms, 在所有 Python3 提交中击败了91.38%的用户
# 内存消耗 :14.2 MB, 在所有 Python3 提交中击败了68.57%的用户

# In[14]:


nums = [2, 7, 11, 15]
target = 9
s = Solution()
result = s.twoSum(nums, target)
print(result)


# In[1]:


a = [1,2,3]
if 3 in a[3:]:
    print('true')
else:
    print('false')


# In[2]:


a[1:].index(2)


# In[3]:


a.index(2)


# In[ ]:




