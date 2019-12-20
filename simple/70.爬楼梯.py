# -*- coding:utf-8 -*-
# @time   : 2019-12-20 08:38
# @author : xulei
# @project: leetcode

"""
标签：腾讯精选练习（50题）
题目：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
"""


# 暴力法-递归：F(i) = F(i-1) + F(i-2)
# 边界：F(0) = 0, F(1) = 1, F(2) = 2
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)
# 16 / 45 个通过测试用例  状态：超出时间限制


# 优化-备忘录算法-保存每个阶段的结果：
# 最优子结构：F(i) = F(i-1) + F(i-2)
# 边界：F(0) = 0, F(1) = 1, F(2) = 2
# 状态转移公式：F(0) = 0, F(1) = 1, F(2) = 2, F(i) = F(i-1) + F(i-2)
class Solution2:
    def climb(self, n: int, mp: dict) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        mp[0], mp[1], mp[2] = 0, 1, 2
        if n in mp.keys():
            return mp[n]
        else:
            value = self.climb(n-1, mp) + self.climb(n-2, mp)
            mp[n] = value
            return value

    def climbStairs(self, n: int) -> int:
        return self.climb(n, dict())
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了91.93%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.66%


# 优化-动态规划-只保存前两个阶段的结果：
# 最优子结构：F(i) = F(i-1) + F(i-2)
# 边界：F(0) = 0, F(1) = 1, F(2) = 2
# 状态转移公式：F(0) = 0, F(1) = 1, F(2) = 2, F(i) = F(i-1) + F(i-2)
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, temp = 1, 2, 0
        for i in range(3, n+1):
            temp = a + b
            a, b = b, temp
        return temp
# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了91.93%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.66%的用户


