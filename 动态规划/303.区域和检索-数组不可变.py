# -*- coding:utf-8 -*-
# @time   : 2019-12-30 15:06
# @author : xulei
# @project: leetcode

"""
标签：简单、动态规划
题目：
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class NumArray1:
    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(sum(self.nums[i:j]), self.nums[j])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 执行出错信息：Line 8: TypeError: 'int' object is not iterable
# 最后执行的输入：
# ["NumArray","sumRange","sumRange","sumRange"]
# [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]


class NumArray2:
    dt = {}

    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if (i, j) not in NumArray2.dt.keys():
            NumArray2.dt[(i, j)] = sum(sum(self.nums[i:j]), self.nums[j])
        return NumArray2.dt[(i, j)]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# 执行出错信息：Line 8: TypeError: 'int' object is not iterable
# 最后执行的输入：
# ["NumArray","sumRange","sumRange","sumRange"]
# [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]


class NumArray3:
    dt = {}

    def __init__(self, nums: list):
        self.nums = nums
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                self.dt[(i, j)] = sum

    def sumRange(self, i: int, j: int) -> int:
        return self.dt[(i, j)]

# 15 / 16 个通过测试用例
# 状态：超出时间限制


# nums[i:j+1] = sum(nums[:j+1]) - sum(nums[:i])
class NumArray4:
    def __init__(self, nums: list):
        self.dp = nums[:]
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1] if i > 0 else self.dp[j]
# 执行结果：通过
# 执行用时 :92 ms, 在所有 python3 提交中击败了87.22%的用户
# 内存消耗 :16.2 MB, 在所有 python3 提交中击败了98.83%


