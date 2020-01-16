# -*- coding:utf-8 -*-
# @time   : 2020-01-15 10:33
# @author : xl
# @project: leetcode

"""
标签：华为、中等、字符串、数学
题目：
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0]*(len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            n1 = num1[i]
            for j in range(len(num2)-1, -1, -1):
                n2 = num2[j]
                sm = res[i+j+1] + int(n1) * int(n2)
                res[i+j+1] = sm % 10
                res[i+j] += sm // 10

        return ''.join([str(x) for x in res]).lstrip('0')

# 执行结果：通过
# 执行用时 :156 ms, 在所有 Python3 提交中击败了51.98% 的用户
# 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了41.57%的用户
