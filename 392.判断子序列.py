# -*- coding:utf-8 -*-
# @time   : 2019-12-30 15:55
# @author : xulei
# @project: leetcode

"""
标签：简单、动态规划、二分查找、贪心算法
题目：
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"
返回 true.

示例 2:
s = "axc", t = "ahbgdc"
返回 false.

后续挑战 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
"""


class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(set(s).difference(set(t))) > 0:
            return False
        ind = 0
        for i in s:
            print(i, ind)
            if i not in t[ind:]:
                return False
            else:
                ind += t[ind:].index(i) + 1
        return True
# 执行结果：通过
# 执行用时 :52 ms, 在所有 python3 提交中击败了78.72%的用户
# 内存消耗 :17.2 MB, 在所有 python3 提交中击败了5.26%的用户


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0
        for i in s:
            print(i, ind)
            if i not in t[ind:]:
                return False
            else:
                ind += t[ind:].index(i) + 1
        return True
# 执行结果：通过
# 执行用时 :28 ms, 在所有 python3 提交中击败了99.35%的用户
# 内存消耗 :17.3 MB, 在所有 python3 提交中击败了5.26%的用户


class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
            else:
                return False
        return True
# 执行结果：通过
# 执行用时 :44 ms, 在所有 python3 提交中击败了85.93%的用户
# 内存消耗 :17.5 MB, 在所有 python3 提交中击败了5.26%的用户
