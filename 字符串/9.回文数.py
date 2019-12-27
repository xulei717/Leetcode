# -*- coding:utf-8 -*-
# @time   : 2019-12-16 09:05
# @author : xulei
# @project: leetcode


"""
标签：简单、腾讯精选练习（50题）、字符串
题目：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
"""

# 用整数的思想解决
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        re, y = 0, x
        while y != 0:
            re = re*10 + y % 10
            y = y // 10
        if re != x:
            return False

        return True
# 执行结果：通过
# 执行用时 :72 ms, 在所有 python3 提交中击败了81.22%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.64%


# 用字符串的思想解决
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        re = list(str(x))
        i, j = 0, -1
        while i < len(re) // 2:
            if re[i] != re[j]:
                return False
            i += 1
            j -= 1

        return True
# 执行结果：通过
# 执行用时 :72 ms, 在所有 python3 提交中击败了81.22%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.64%




