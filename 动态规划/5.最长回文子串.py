# -*- coding:utf-8 -*-
# @time   : 2019-12-19 08:49
# @author : xulei
# @project: leetcode

"""
标签：中等、动态规划、腾讯精选练习（50题）
题目：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""


# 判断字符串是不是回文
def isPlalindrome(s: str) -> bool:
    if s == ''.join(reversed(list(s))):
        return True
    else:
        return False


# 暴力法:选出所有子字符串可能的开始和结束位置，并检验它是不是回文
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        mx = ''
        for ic in range(len(s)):
            ch, ss = s[ic], s[ic:]
            if len(mx) >= len(ss):
                break
            while len(ss) > 0:
                i, j = ss.index(ch), ss.rindex(ch)
                if i <= j:
                    if ss[i:j+1] == ''.join(reversed(list(ss[i:j+1]))):
                    # if isPlalindrome(ss[i:j+1]):
                        if len(ss[i:j+1]) > len(mx):
                            mx = ss[i:j+1]
                        # print(ch, i, j, ss[i:j + 1], ss)
                        break
                    else:
                        ss = ss[i:j]
                else:
                    break
            # print(lr)

        return mx
# 101 / 103 个通过测试用例  状态：超出时间限制
# 执行结果：通过
# 执行用时 :7048 ms, 在所有 python3 提交中击败了5.00%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.03%
'''
复杂度分析
时间复杂度：O(n^3)
空间复杂度：O(1)
'''


# 最长公共子串:将字符串s反转得到字符串rev，再求他们的最长公共子串，
# 再判断该最长公共子串是否就是我们要找的最长回文子串，需增加个判断反转字符串的最长公共子串是否和原字符串位置一致。
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        mx = ''
        rev = ''.join(reversed(list(s)))
        for i in range(len(s)):
            ss = ''
            for j in range(i, len(s)):
                ss += s[j]
                if len(ss) <= len(mx):
                    continue
                if isPlalindrome(ss) and ss == rev[len(s)-1-j:len(s)-i]:
                    mx = ss

        return mx
# 41 / 103 个通过测试用例 状态：超出时间限制

# 动态规划:问题建模-中心扩展算法：回文中心的两侧互为镜像。因此，回文可以从它的中心展开，并且只有2n−1个这样的中心。
# 最优子结构：P(i,j) = P(i+1,j-1) + S(i) == S(j) (奇数) ; P(i,i+1) = S(i) == S(i+1) (偶数)
# 边界：P(i,i) = True ； P(i,i+1) = S(i) == S(i+1)  (中心)
# 状态转移公式：P(i,j) = P(i+1,j-1) + S(i) == S(j) (奇数) ; P(i,i+1) = S(i) == S(i+1) (偶数)
class Solution3:
    def expandAroundCenter(self, s: str, left, right) -> str:
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        mx = ''
        for i in range(len(s)):
            s1 = self.expandAroundCenter(s, i, i)
            s2 = self.expandAroundCenter(s, i, i+1)
            mx = max(mx, s1, s2, key=len)

        return mx
# 执行结果：通过
# 执行用时 :312 ms, 在所有 python3 提交中击败了83.07%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.63%


# manacher算法:字符串前后和中间都添加一个#，使字符串变成奇数长度，再使用中心扩展方法
class Solution4:
    def expandAroundCenter(self, s: str, left, right) -> str:
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        mx = ''
        test = '#' + '#'.join(s) + '#'
        for i in range(len(test)):
            mx = max(mx, self.expandAroundCenter(test, i, i), key=len)

        return mx.replace('#', '')
# 执行结果：通过
# 执行用时 :924 ms, 在所有 python3 提交中击败了72.71%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.54%


if __name__ == '__main__':
    sol = Solution2()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ss = 500
    result = sol.longestPalindrome(s)
    print(len(result), result)  # adada
    '''
    "babadada"
    b 0 2 bab babadada
    ['bab']
    a 0 6 abadada abadada
    a 0 4 abada abadad
    a 0 2 aba abad
    ['bab', 'aba']
    b 0 0 b badada
    ['bab', 'aba', 'b']
    a 0 4 adada adada
    ['bab', 'aba', 'b', 'adada']
    adada
    '''
