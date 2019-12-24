# -*- coding:utf-8 -*-
# @time   : 2019-12-24 09:24
# @author : xulei
# @project: leetcode

"""
标签：腾讯精选练习（50题）
题目：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""


import sys
# n^2
class Solution1:
    def maxSubArray(self, nums) -> int:
        mi = 0 - sys.maxsize - 1
        re = [mi] * len(nums)
        for ll in range(len(nums)):
            for i in range(len(nums)):
                if i + ll + 1 > len(nums):
                    break
                re[ll] = max(re[ll], sum(nums[i:i+ll+1]))
        return max(re)
# 199 / 202 个通过测试用例  状态：超出时间限制


import sys
import numpy
import copy
# 备忘录算法:上三角矩阵
# P(i,j) = P(i, j-1) + P(j-1,j)
class Solution2:
    def maxSubArray(self, nums) -> int:
        mil = 0 - sys.maxsize - 1
        # r = [copy.deepcopy(mil) * (len(nums)+1)] * len(nums)
        # re = copy.deepcopy(r)
        re = []
        for t in range(len(nums)):
            re.append([mil] * (len(nums)+1))
        # print(id(r), id(re))
        print(len(re), len(re[0]))
        print(re)
        for n in range(len(nums)):
            print(id(re[n]))
            re[n][n+1] = nums[n]
            print(n, re[n][n+1])
        print(re)
        for i in range(len(nums)):
            for j in range(i+2, len(nums)+1):
                re[i][j] = re[i][j-1] + re[j-1][j]
                print(i, j, re[i][j])
        return numpy.max(re)
# 200 / 202 个通过测试用例  状态：超出内存限制


import sys
# 动态规划:上三角矩阵 n^2
# P(i,j) = P(i, j-1) + P(j-1,j)
# P(j-1,j) = nums[j-1:j]
class Solution3:
    def maxSubArray(self, nums) -> int:
        re = 0 - sys.maxsize - 1
        print(len(nums))
        for i in range(len(nums)):
            j = i + 1
            print(i, j, nums[i:j])
            p = nums[i:j][0]
            re = max(re, p)
            while j < len(nums):
                j += 1
                p += nums[j-1:j][0]
                re = max(re, p)
                print(i, j, re)
        return re
# 200 / 202 个通过测试用例  状态：超出时间限制


# 动态规划：每一步都选择最佳方案，到最后就是全局最优的方案。n
# 遍历数组并在每个步骤中更新：当前元素，当前元素位置的最大和，迄今为止的最大和
class Solution4:
    def maxSubArray(self, nums) -> int:
        cur, ma = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur+nums[i])
            ma = max(ma, cur)
        return ma
# 执行结果：通过
# 执行用时 :292 ms, 在所有 python3 提交中击败了5.00%的用户
# 内存消耗 :32.8 MB, 在所有 python3 提交中击败了5.04%


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s3 = Solution3()
    print(s3.maxSubArray(nums))

