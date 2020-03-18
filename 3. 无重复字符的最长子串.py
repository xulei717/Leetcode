# -*- coding:utf-8 -*-
# @time   : 2020-01-15 09:44
# @author : xl
# @project: leetcode

"""
标签：中等、字符串、哈希表、双指针、滑动窗口 Sliding Window、华为
题目：
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""

'''
这道题主要用到思路是：滑动窗口

什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：O(n)O(n)O(n)

作者：powcai
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '' or s is None:
            return 0
        ls, ma = [], 0
        for i in range(len(s)):
            c = s[i]
            if c in ls:
                ma = max(ma, len(ls))
                ind = ls.index(c)
                ls = ls[ind+1:]
            ls.append(c)
            if len(s) - i + len(ls) < ma:
                return ma
        ma = max(ma, len(ls))

        return ma
# 执行结果：通过
# 执行用时 :276 ms, 在所有 Python3 提交中击败了17.17% 的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.38%的用户

# 提前终止
# if len(s) - i + len(ls) < ma:
#     return ma
# 执行结果：通过
# 执行用时 :296 ms, 在所有 Python3 提交中击败了16.65% 的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了34.20%的用户
