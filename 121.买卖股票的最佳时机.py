# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:52
# @author : xulei
# @project: leetcode

"""
标签：简单、动态规划、股票、腾讯精选练习（50题）
题目：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""


class Solution1:
    def maxProfit(self, prices: list) -> int:
        re = 0
        for i in range(len(prices) - 1):
            re = max(re, max(prices[i+1:]) - prices[i])

        return re
# 199 / 200 个通过测试用例  状态：超出时间限制

import sys
class Solution2:
    def maxProfit(self, prices: list) -> int:
        if prices is None or len(prices) == 0:
            return 0
        maxprices, minprice = 0, sys.maxsize
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                maxprices = max(maxprices, prices[i] - minprice)

        return maxprices
# 执行结果：通过
# 执行用时 :64 ms, 在所有 python3 提交中击败了98.88%的用户
# 内存消耗 :13.6 MB, 在所有 python3 提交中击败了99.46%


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
# i:0-len(prices)-1; k = 1
import sys
class Solution3:
    def maxProfit(self, prices: list) -> int:
        if prices is None or len(prices) == 0:
            return 0
        dp_i_0, dp_i_1 = 0, 0 - sys.maxsize - 1
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])

        return dp_i_0
# 执行结果：通过
# 执行用时 :84 ms, 在所有 python3 提交中击败了58.42%的用户
# 内存消耗 :13.7 MB, 在所有 python3 提交中击败了97.73%的用户
