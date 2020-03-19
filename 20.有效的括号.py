# coding: utf-8

# -- coding:utf-8 --
# @time : 2020-3-2 20:40
# @author : xulei
# @project: leetcode


"""
标签：简单、栈、字符串
题目：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def isValid(self, s: str) -> bool:
        cl = []
        for c in s:
            print(c)
            if c in ['(', '[', '{']:
                cl.append(c)
            else:
                if c == ')' and len(cl) > 0 and cl[-1] == '(':
                    cl.pop(-1)
                    print('c:)', len(cl), cl)
                elif c == ']' and len(cl) > 0 and cl[-1] == '[':
                    cl.pop(-1)
                elif c == '}' and len(cl) > 0 and cl[-1] == '{':
                    cl.pop(-1)
                else:
                    return False
            print(c, cl)

        if len(cl) == 0:
            return True
        else:
            return False
# 执行结果：通过
# 执行用时 :36 ms, 在所有 Python3 提交中击败了62.53%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了23.89%的用户

st = Solution()
s = '()'
rt = st.isValid(s)
print(rt)