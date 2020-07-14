#!/usr/bin/env python
# coding: utf-8

# # -*- coding:utf-8 -*-
# # @time   : 2020-7-14 11:00
# # @author : xulei
# # @project: leetcode

"""
标签：中等、数组、动态规划
题目：
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。



例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。



说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

import sys

'''
动态规划
f[0][0] = triangle[0][0]
f[i][0] = f[i-1][0] + c[i][0]
f[i][i] = f[i-1][i-1] + c[i][i]
f[i][j] = min(f[i-1][j], f[i-1][j-1]) + c[i][j]
'''
class Solution:  # 只求最后一行各位置上的最小和，有重复计算的过程
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        i, j = len(triangle) - 1, len(triangle[-1])
        mi = sys.maxsize
        for k in range(j):
            mi = min(mi, self.f(i, k, triangle))
        return mi

    def f(self, m, n, t: list[list[int]]):
        if m == 0 and n == 0:
            return t[0][0]
        elif n == 0:
            return self.f(m - 1, 0, t) + t[m][0]
        elif m == n:
            return self.f(m - 1, m - 1, t) + t[m][m]
        else:
            return min(self.f(m - 1, n, t), self.f(m - 1, n - 1, t)) + t[m][n]

# 执行结果：超出时间限制

# 动态规划：采用 二维矩阵，记录每一步骤的和，时间复杂度O(n^2)，空间复杂度O(n^2)
import sys
class Solution1:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        f = [[sys.maxsize]*m for _ in range(m)]
        f[0][0] = triangle[0][0]
        for i in range(1,m):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1,i):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[-1])
# 执行结果：通过
# 执行用时 :56 ms, 在所有 Python3 提交中击败了28.61%的用户
# 内存消耗 :14.9 MB, 在所有 Python3 提交中击败了9.09%的用户

# 动态规划+空间优化：采用 使用两个长度为 n 的一维数组进行转移，将 i 根据奇偶性映射到其中一个一维数组，
# 那么 i−1就映射到了另一个一维数组。这样我们使用这两个一维数组，交替地进行状态转移。
# 时间复杂度O(n^2)，空间复杂度O(n)
import sys
class Solution2:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        f = [[sys.maxsize]*m for _ in range(2)]
        f[0][0] = triangle[0][0]
        for i in range(1,m):
            cur, pre = i%2, 1-i%2
            f[cur][0] = f[pre][0] + triangle[i][0]
            for j in range(1,i):
                f[cur][j] = min(f[pre][j], f[pre][j-1]) + triangle[i][j]
            f[cur][i] = f[pre][i-1] + triangle[i][i]
        return min(f[(m-1)%2])

# 执行结果：通过
# 执行用时 :48 ms, 在所有 Python3 提交中击败了71.45%的用户
# 内存消耗 :14 MB, 在所有 Python3 提交中击败了18.18%的用户
