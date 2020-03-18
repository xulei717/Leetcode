# -*- coding:utf-8 -*-
# @time   : 2020-01-17 09:10
# @author : xl
# @project: leetcode

"""
标签：中等、贪心算法、排序+插入
题目：
假设有打乱顺序的一群人站成一个队列。
每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
"""

'''
算法：
1.排序
（1）按照高度h降序排列
（2）在同一个高度的人中，按K值的升序排列
2.插入：逐个把它们放在输出队列中，索引等于i它们的K值
'''
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

# 执行结果：通过
# 执行用时 :44 ms, 在所有 Python3 提交中击败了99.61% 的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了56.96%的用户
