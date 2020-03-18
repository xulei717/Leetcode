# -*- coding:utf-8 -*-
# @time   : 2019-12-25 16:37
# @author : xulei
# @project: leetcode

"""
标签：困难、动态规划、股票
题目：
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
"""


# 动态规划
"""
状态转移方程总结一下：

base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：i表示数组下标，k表示交易次数，0表示无持有股票，1表示持有股票
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

作者：labuladong
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
"""
# i:0-len(prices)-1; k = 2
import sys
class Solution:
    def maxProfit(self, prices: list) -> int:
        if prices is None or len(prices) == 0:
            return 0
        dp_i_0_0, dp_i_0_1 = 0, 0 - sys.maxsize - 1
        dp_i_1_0, dp_i_1_1 = 0, 0 - sys.maxsize - 1
        for i in range(len(prices)):
            dp_i_0_0 = max(dp_i_0_0, dp_i_0_1 + prices[i])
            dp_i_0_1 = max(dp_i_0_1,  - prices[i])
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + prices[i])
            dp_i_1_1 = max(dp_i_1_1, dp_i_0_0 - prices[i])

        return dp_i_1_0
# 执行结果：通过
# 执行用时 :84 ms, 在所有 python3 提交中击败了96.05%的用户
# 内存消耗 :13.7 MB, 在所有 python3 提交中击败了99.36%

