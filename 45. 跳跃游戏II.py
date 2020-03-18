# -*- coding:utf-8 -*-
# @time   : 2020-01-17 09:52
# @author : xl
# @project: leetcode

"""
标签：困难、贪心算法、数组
题目：
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释:  跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

说明:
假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
"""


# 从0位置开始，看每一步可以达到的最远的位置，看最终包括了最后一个位置就返回当前步数
class Solution1:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return 0
        last = len(nums) - 1
        mm, i, step = 0, 0, 0
        while i <= mm:
            mm = max(mm, i+nums[i])
            if mm >= last:
                return step + 1
            step += 1
            ma = 0
            for x in range(i+1, mm+1):
                if x + nums[x] >= ma:
                    i = x
                    ma = x + nums[i]

# 执行结果：通过
# 执行用时 :56 ms, 在所有 Python3 提交中击败了99.21% 的用户
# 内存消耗 :14.5 MB, 在所有 Python3 提交中击败了100%的用户
