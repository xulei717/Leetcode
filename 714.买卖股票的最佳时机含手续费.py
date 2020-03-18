# -*- coding:utf-8 -*-
# @time   : 2019-12-26 14:25
# @author : xulei
# @project: leetcode

"""
标签： 中等、动态规划、股票
题目：
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""


# 动态规划
"""
状态转移方程总结一下：

base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：i表示数组下标，k表示交易次数，0表示无持有股票，1表示持有股票
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i] - fee)

作者：labuladong
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
"""
# i:0-len(prices)-1; k = n
import sys
class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        if prices is None or len(prices) <= 1:
            return 0
        dp_i_0, dp_i_1 = 0, 0 - sys.maxsize - 1
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)

        return dp_i_0
# 执行结果：通过
# 执行用时 :876 ms, 在所有 python3 提交中击败了84.99%的用户
# 内存消耗 :19.8 MB, 在所有 python3 提交中击败了6.45%



