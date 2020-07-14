#!/usr/bin/env python
# coding: utf-8

# # -*- coding:utf-8 -*-
# # @time   : 2020-7-14 09:48
# # @author : xulei
# # @project: leetcode

"""
标签：简单、位运算
题目：
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution1:
    def intStr(self, n):
        if n==0:
            return ""
        else:
            return self.intStr(n//2)+str(n%2)

    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        zs = self.intStr(z)
        num = zs.count("1")
        # print(zs)
        # print(num)
        return num


# 执行结果：通过
# 执行用时 :48 ms, 在所有 Python3 提交中击败了19.96%的用户
# 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.67%的用户

# 采用 python 自带了方法 bin 函数，比如 bin(12345) 回返回字符串 '0b11000000111001', 这个时候在把0b去掉即可
class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        zs = bin(z).replace('0b', '')
        num = zs.count("1")
        # print(zs)
        # print(num)
        return num

# 执行结果：通过
# 执行用时 :36 ms, 在所有 Python3 提交中击败了88.06%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了6.67%的用户

# 采用字符串的 format 方法来获取二进制
class Solution3:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        zs = '{0:b}'.format(z)
        num = zs.count("1")
        # print(zs)
        # print(num)
        return num

# 执行结果：通过
# 执行用时 :40 ms, 在所有 Python3 提交中击败了70.14%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了6.67%的用户
