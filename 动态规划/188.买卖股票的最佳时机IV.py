# -*- coding:utf-8 -*-
# @time   : 2019-12-25 16:37
# @author : xulei
# @project: leetcode

"""
标签： 困难、动态规划、股票
题目：
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
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
# i:0-len(prices)-1; k = k
import sys
class Solution1:
    def maxProfit122(self, prices: list) -> int:
        if prices is None or len(prices) == 0:
            return 0
        dp_i_0, dp_i_1 = 0, 0 - sys.maxsize - 1
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])

        return dp_i_0

    def maxProfit(self, k: int, prices: list) -> int:
        if prices is None or len(prices) == 0 or k < 1:
            return 0
        k = min(k, len(prices) // 2)
        if k >= 5000:  # 当做操作次数是无限的
            return self.maxProfit122(prices)

        dp_i_0, dp_i_1 = [0] * k, [0 - sys.maxsize - 1] * k
        for i in range(len(prices)):
            pre_0 = 0
            for kk in range(k):
                temp = dp_i_0[kk]
                dp_i_0[kk] = max(dp_i_0[kk], dp_i_1[kk] + prices[i])
                dp_i_1[kk] = max(dp_i_1[kk], pre_0 - prices[i])
                pre_0 = temp

        return dp_i_0[k-1]
# 1.209 / 211 个通过测试用例  状态：执行出错
# Line 5: MemoryError  dp_i_0, dp_i_1 = [0] * k, [0 - sys.maxsize - 1] * k
# 2.增加： k = min(k, len(prices) // 2)
# 209 / 211 个通过测试用例  状态：超出时间限制
# 3.增加判断条件：k >= 5000:  # 当做操作次数是无限的
# 执行结果：通过
# 执行用时 :112 ms, 在所有 python3 提交中击败了95.87%的用户
# 内存消耗 :13.3 MB, 在所有 python3 提交中击败了100.00%的用户
