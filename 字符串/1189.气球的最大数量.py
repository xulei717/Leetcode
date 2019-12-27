# -*- coding:utf-8 -*-
# @time   : 2019-12-09 16:46
# @author : xulei
# @project: leetcode

'''
标签：简单、字符串

题目：
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

示例 1：
输入：text = "nlaebolko"
输出：1
示例 2：
输入：text = "loonbalxballpoon"
输出：2
示例 3：
输入：text = "leetcode"
输出：0

提示：
1 <= text.length <= 10^4
text 全部由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
'''

#1.遍历字符串，统计每个字符出现的次数
class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        bl, al, ll, ol, nl = 0, 0, 0, 0, 0
        for i in text:
            if i == 'b':
                bl += 1
            elif i == 'a':
                al += 1
            elif i == 'l':
                ll += 1
            elif i == 'o':
                ol += 1
            elif i == 'n':
                nl += 1

        return min(bl, al, int(ll/2), int(ol/2), nl)

# 执行结果：通过
# 执行用时 :40 ms, 在所有 python3 提交中击败了91.45%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了100.00%的用户

#2.遍历字符串，统计每个字符出现的次数，用Python list自带的函数count计算字符串中某个字符出现的次数
class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        result = [text.count(x) if x not in ['l', 'o'] else int(text.count(x)/2) for x in ['b', 'a', 'l', 'o', 'n']]
        return min(result)


# 执行结果：通过
# 执行用时 :28 ms, 在所有 python3 提交中击败了99.78%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了100.00%的用户


