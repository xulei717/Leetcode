#!/usr/bin/env python
# coding: utf-8

# # -*- coding:utf-8 -*-
# # @time   : 2020-7-15 09:00
# # @author : xulei
# # @project: leetcode

"""
标签：中等、树、动态规划、数学
题目：
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 动态规划：定义函数
# g(n)：长度为n的序列能构成的不同二叉搜索树的个数, g[0] = g[1] = 1
# f(i, n)：以i为根、长度为n的不同二叉搜索树的个数（i<=i<=n）
# f(i, n) = g(i-1)*g(n-i)  选择数字 i 作为根，则根为 i 的所有二叉搜索树的集合是左子树集合和右子树集合的笛卡尔积
# g(n) = ∑f(i,n)  (i属于[1,...,n])
# 时间复杂度是O(n^2)，空间复杂度是O(n)
class Solution1:
    def numTrees(self, n: int) -> int:
        g = [0]*(n+1)
        g[0], g[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                g[i] += g[j-1]*g[i-j]
            # print(i,g[i])

        return g[n]


# 执行结果：通过
# 执行用时 :36 ms, 在所有 Python3 提交中击败了85.25%的用户
# 内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.26%的用户

