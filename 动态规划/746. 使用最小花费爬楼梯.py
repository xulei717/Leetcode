# -*- coding:utf-8 -*-
# @time   : 2019-12-30 16:15
# @author : xulei
# @project: leetcode

"""
标签：简单、动态规划、数组、走阶梯
题目：
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：
cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
"""

# 动态规划
# 临界条件：
# len == 1, return 0
# len == 2, return min(cost[0], cost[1])
# 转移函数：
# f(n) = min(f(n-1), f(n-2) + cost[n])
class Solution1:
    def minCostClimbingStairs(self, cost: list) -> int:
        if cost is None or len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        f_n1, f_n2 = min(cost[0], cost[1]), 0
        re = min(f_n1, f_n2 + cost[2])
        for i in range(3, len(cost)):
            f_n2 = f_n1
            f_n1 = re
            re = min(f_n1, f_n2 + cost[i])
        return re
'''
54 / 276 个通过测试用例
状态：解答错误
输入：
[0,0,1,1]
输出：
0
预期：
1
'''


# 动态规划
# 边界条件：
# f(n) = cost[n], n <= 1
# 转移函数：
# f(n) = min(f(n-1), f(n-2)) + cost[n]
class Solution2:
    def minCostClimbingStairs(self, cost: list) -> int:
        if cost is None or len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        f_n1, f_n2 = cost[1], cost[0]
        re = min(f_n1, f_n2) + cost[2]
        for i in range(3, len(cost)):
            f_n2 = f_n1
            f_n1 = re
            re = min(f_n1, f_n2) + cost[i]
        return min(re, f_n1)
# 执行结果：通过
# 执行用时 :92 ms, 在所有 python3 提交中击败了14.85%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了98.95%的用户


class Solution3:
    def minCostClimbingStairs(self, cost: list) -> int:
        _len = len(cost)
        if _len < 2:
            return 0
        else:
            dp = [0] * _len
            dp[:2] = cost[:2]
            for i in range(2, _len):
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            return min(dp[-1], dp[-2])
# 执行结果：通过
# 执行用时 :64 ms, 在所有 python3 提交中击败了90.42%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了98.95%的用户
