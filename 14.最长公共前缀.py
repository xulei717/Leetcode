# -*- coding:utf-8 -*-
# @time   : 2019-12-18 08:46
# @author : xulei
# @project: leetcode

"""
标签：简单、二分查找、字符串、腾讯精选练习（50题）
题目：
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
"""


# 水平扫描：找到最短的字符串长度，然后从前往后枚举字符串的每一列，不同则break
class Solution1:
    def longestCommonPrefix(self, strs: list) -> str:
        result = ''
        if strs is None or len(strs) == 0:
            return result
        lmin = min([len(x) for x in strs])
        for i in range(lmin):
            cs = [x[i] for x in strs]
            if len(set(cs)) == 1:
                result += cs[0]
            else:
                break

        return result
# 执行结果：通过
# 执行用时 :28 ms, 在所有 python3 提交中击败了99.37%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.59%的用户


class Solution11:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        if strs is None or len(strs) == 0:
            return result
        for cs in zip(*strs):
            if len(set(cs)) == 1:
                result += cs[0]
            else:
                break

        return result
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了97.51%的用户
# 内存消耗 :12.6 MB, 在所有 python3 提交中击败了99.71%的用户

# 二分查找
class Solution2:
    def isCommonPrefix(self, strs: list[str], middle: int) -> bool:
        pre = strs[0][:middle]
        for st in strs:
            if pre != st[:middle]:
                return False
        return True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        if strs is None or len(strs) == 0:
            return result
        lmin = min([len(x) for x in strs])
        low, heigh = 1, lmin  # 因为Python列表是左闭右开，所以low赋值为1，height赋值为lmin
        while low <= heigh:
            middle = (low + heigh) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                heigh = middle - 1

        return strs[0][:(low + heigh) // 2]
# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了92.83%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.65%的用户
