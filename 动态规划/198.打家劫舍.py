# -*- coding:utf-8 -*-
# @time   : 2019-12-30 14:33
# @author : xulei
# @project: leetcode

"""
标签：简单、动态规划
题目：
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
"""
'''
f(k)：表示从前k个房屋中能抢劫到的最大数额，Ai：表示第i个房屋的钱数。
n = 1,f(1) = A1
n = 2,f(2) = max(A1，A2)
n = 3,
 1.抢第三个房子，总数额是第1个房子加上第3个房子
 2.不抢第三个房子，返回最大额度的房子额度值
转移公式：f(k) = max(f(k-2)+Ak, f(k-1))
'''


class Solution1:
    def rob(self, nums: list) -> int:
        if nums is None or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))
# 49 / 69 个通过测试用例  状态：超出时间限制


class Solution2:
    def rob(self, nums: list) -> int:
        if nums is None or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        f_k2, f_k1 = nums[0] + nums[2], max(nums[0], nums[1])
        re = max(f_k1, f_k2)
        for i in range(3, len(nums)):
            f_k2 = f_k1
            f_k1 = re
            re = max(f_k2 + nums[i], f_k1)

        return re
# 执行结果：通过
# 执行用时 :48 ms, 在所有 python3 提交中击败了26.01%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.40%
