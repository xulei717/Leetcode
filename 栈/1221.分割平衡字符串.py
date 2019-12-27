# -*- coding:utf-8 -*-
# @time   : 2019-12-09 16:16
# @author : xulei
# @project: leetcode

'''
标签：简单、字符串、栈
题目：
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量。

示例 1：
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 2：
输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 3：
输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".
 
提示：
1 <= s.length <= 1000
s[i] = 'L' 或 'R'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
'''

#1.遍历字符串，用栈记录中间结果
class Solution1:
    def balancedStringSplit(self, s: str) -> int: #RLRRLLRLRL
        result = []
        tmp = [s[0]]
        tt = s[0]
        for i in s[1:]:
            if len(tmp) == 0:
                tmp.append(i)
                tt = i
            else:
                if i != tmp[-1]:
                    tt += i
                    del tmp[-1]
                    if len(tmp) == 0:
                        result.append(tt)
                        tt = ""
                else:
                    tt += i
                    tmp.append(i)

        return len(result)

# 执行结果：通过
# 执行用时 :52 ms, 在所有 python3 提交中击败了15.58%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户

#2.遍历字符串，用栈记录中间结果
class Solution2:
    def balancedStringSplit(self, s: str) -> int: #RLRRLLRLRL
        result = []
        tmp = [s[0]]
        tt = s[0]
        for i in s[1:]:
            if len(tmp) == 0:
                tmp.append(i)
                tt = i
            elif i != tmp[-1]:
                tt += i
                del tmp[-1]
                if len(tmp) == 0:
                    result.append(tt)
                    tt = ""
            else:
                tt += i
                tmp.append(i)

        return len(result)

# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了95.92%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了100.00%的用户


'''
涉及的知识点：栈、贪心算法
'''


