# -*- coding:utf-8 -*-
# @time   : 2020-01-15 14:00
# @author : xl
# @project: leetcode

"""
标签：华为、中等、回溯算法-深度优先搜索策略+约束函数、字符串
题目：
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
"""

# IP地址是由一个32位的二进制数所构成
# 2^8 -1 = 256 -1 = 255
# one value: [0, 1, ..., 255]; len(value): 1-3
# len(s): 4-12


# 回溯 + 递归
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def track(count=0, ip='', s=''):
            if count == 4:
                if s == '':
                    res.append(ip[:-1])
                return
            if 0 < len(s) <= (4-count)*3:
                track(count+1, ip+s[0]+'.', s[1:])
            if 1 < len(s) <= (4-count)*3 and s[0] != '0':
                track(count+1, ip+s[:2]+'.', s[2:])
            if 2 < len(s) <= (4-count)*3 and int(s[:3]) < 256 and s[0] != '0':
                track(count+1, ip+s[:3]+'.', s[3:])
        track(0, '', s)

        return res
# 执行结果：通过
# 执行用时 :28 ms, 在所有 Python3 提交中击败了98.30% 的用户
# 内存消耗 :13.3 MB, 在所有 Python3 提交中击败了5.15%的用户


