# -*- coding:utf-8 -*-
# @time   : 2020-01-16 17:33
# @author : xl
# @project: leetcode

"""
标签：中等、数学、随机、拒绝采样 Rejection Sampling
题目：
给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。

说明:

    输入值和输出值都将是浮点数。
    圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
    圆周上的点也认为是在圆中。
    randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。

示例 1：

输入:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
输出: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

示例 2：

输入:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
输出: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

输入语法说明：

输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有三个参数，圆的半径、圆心的 x 坐标、圆心的 y 坐标。randPoint 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-random-point-in-a-circle
"""

import random
import math
class Solution1:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x0 = x_center
        self.y0 = y_center

    def randPoint(self) -> list[float]:
        x = random.uniform(self.x0 - self.r, self.x0 + self.r)
        yd = math.sqrt((self.r**2 - (abs(self.x0-x)**2)))
        y = random.uniform(self.y0-yd, self.y0+yd)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# 执行结果：解答错误


import random
import math
class Solution2:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x0 = x_center
        self.y0 = y_center

    def randPoint(self) -> list[float]:
        xl = self.x0 - self.r
        yl = self.y0 - self.r
        while True:
            x = random.random()*self.r*2 + xl
            y = random.random()*self.r*2 + yl
            if math.pow((x-self.x0), 2)+math.pow((y-self.y0), 2) <= math.pow(self.r, 2):
                return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# 执行结果：通过
# 执行用时 :180 ms, 在所有 Python3 提交中击败了63.86% 的用户
# 内存消耗 :23.3 MB, 在所有 Python3 提交中击败了68.57%的用户
