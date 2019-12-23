# -*- coding:utf-8 -*-
# @time   : 2019-12-23 09:04
# @author : xulei
# @project: leetcode

"""
标签：腾讯精选练习（50题）
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:
输入: m = 7, n = 3
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
"""


# 迭代
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n <= 0:
            return 0
        if m * n <= 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
# 执行结果：超出时间限制  37 / 62 个通过测试用例


# 备忘录算法
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n <= 0:
            return 0
        if m * n <= 1:
            return 1
        mn = dict()
        if (m, n) in mn.keys():
            return mn[(m, n)]
        else:
            value = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
            mn[(m, n)] = value
            return value
# 37 / 62 个通过测试用例  状态：超出时间限制


# 备忘录算法
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n <= 0:
            return 0
        if m * n <= 1:
            return 1
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了83.95%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了98.84%


# 排列组合:C((m-1)/(m+n-2))
import math
class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
# 执行结果：通过
# 执行用时 :44 ms, 在所有 python3 提交中击败了50.79%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了98.84%的用户


# 动态规划:空间复杂度 O(2n)
class Solution5:
    def uniquePaths(self, m: int, n: int) -> int:
        pre, cur = [1]*n, [1]*n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j-1] + pre[j]
            pre = cur[:]
        return cur[-1]
# 执行结果：通过
# 执行用时 :44 ms, 在所有 python3 提交中击败了50.79%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了98.84%的用户


# 动态规划:空间复杂度 O(n)
class Solution6:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了83.95%的用户
# 内存消耗 :12.6 MB, 在所有 python3 提交中击败了98.97%

