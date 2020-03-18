# -*- coding:utf-8 -*-
# @time   : 2019-12-26 14:25
# @author : xulei
# @project: leetcode

"""
标签： 中等、动态规划、股票
题目：
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""


# 动态规划
"""
状态转移方程总结一下：

base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：i表示数组下标，k表示交易次数，0表示无持有股票，1表示持有股票
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-2][0] - prices[i])

作者：labuladong
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
"""
# i:0-len(prices)-1; k = n
import sys
class Solution:
    def maxProfit(self, prices: list) -> int:
        if prices is None or len(prices) <= 1:
            return 0
        dp_i_0, dp_i_1, pre_i = 0, 0 - sys.maxsize - 1, 0
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, pre_i - prices[i])
            pre_i = temp

        return dp_i_0
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了99.83%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户



