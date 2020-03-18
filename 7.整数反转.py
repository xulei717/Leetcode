# -*- coding:utf-8 -*-
# @time   : 2019-12-13 09:06
# @author : xulei
# @project: leetcode


"""
标签：简单、数学、腾讯精选练习（50题）
题目：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−(2的31次方),  （2的31次方） − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
"""


class Solution1:
    def reverse(self, x: int) -> int:
        result, y = 0, abs(x)
        while y > 0:
            result = result * 10 + y % 10
            y = y // 10
        if x < 0:
            result = 0 - result
        if result < 0 - pow(2, 31) or result > pow(2, 31) - 1:
            return 0

        return result
# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了93.88%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.88%的用户

#在计算过程中进行判断
#Python中-123%10=7,所以运算过程中需要都当成正数进行处理
class Solution2:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = pow(2, 31) - 1, 0 - pow(2, 31)
        result, y = 0, abs(x)
        while y != 0:
            pop = y % 10
            y = y // 10
            # 判断数值是否溢出
            if x > 0 and (result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7)):
                return 0
            if x < 0 and (result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 8)):
                return 0
            result = result * 10 + pop
        if x < 0:
            result = 0 - result

        return result
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了98.11%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.88%的用户

# 把整数转换成列表，然后通过索引乘以10的次方，刚好下标就是次方，然后累加
# 不断叠加的是正数最大位的数
class Solution3:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = pow(2, 31) - 1, 0 - pow(2, 31)
        print(INT_MAX)  # 2147483647
        result = 0
        # lx = [int(_) for _ in str(abs(x))]
        lx = list(str(abs(x)))
        for i in range(len(lx)):
            pop = pow(10, i) * int(lx[i])
            if x > 0 and (INT_MAX - pop < result):
                return 0
            if x < 0 and (INT_MAX - pop < result + 1):
                return 0
            result += pop
            print(i, pop, result)
        if x < 0:
            result = 0 - result

        return result
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了98.11%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.86%的用户

