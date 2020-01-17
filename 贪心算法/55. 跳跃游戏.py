# -*- coding:utf-8 -*-
# @time   : 2020-01-17 09:52
# @author : xl
# @project: leetcode

"""
标签：中等、贪心算法、数组
题目：
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
"""


# 计算当前元素能否达到右边最近的能够达到最后一个元素的元素-可获得一种解，每次尽量跳最少步数的解
class Solution1:
    def canJump(self, nums: list[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= last - i:
                last = i
        if last == 0:
            return True
        return False

# 执行结果：通过
# 执行用时 :36 ms, 在所有 Python3 提交中击败了100.00% 的用户
# 内存消耗 :14.6 MB, 在所有 Python3 提交中击败了99.56%的用户

