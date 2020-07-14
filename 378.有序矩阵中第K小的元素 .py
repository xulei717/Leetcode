#!/usr/bin/env python
# coding: utf-8

# # -*- coding:utf-8 -*-
# # @time   : 2020-7-2 21:48
# # @author : xulei
# # @project: leetcode

"""
标签：中等、堆、二分查找
题目：
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。



示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。



提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 排序
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ls = []
        for i in range(len(matrix)):
            ls = ls + matrix[i]
        ls_sort = sorted(ls)

        return ls_sort[k-1]

# 执行结果：通过
# 执行用时 :292 ms, 在所有 Python3 提交中击败了23.6%的用户
# 内存消耗 :19.9 MB, 在所有 Python3 提交中击败了6.67%的用户

