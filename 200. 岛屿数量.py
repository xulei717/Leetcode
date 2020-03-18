# -*- coding:utf-8 -*-
# @time   : 2020-01-15 15:47
# @author : xl
# @project: leetcode

"""
标签：中等、深度优先搜索、广度优先搜索、并查集、华为
题目：
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
"""


# 深度优先搜索DFS-栈的思路，没用到栈
class Solution1:
    def numIslands(self, grid: list[list[str]]) -> int:
        nums = 0
        row = len(grid)
        r = 0

        def dfs(i, j):
            grid[i][j] = '0'
            # 按照上、下、左、右的顺序进行搜索
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ix = i + x
                jy = j + y
                if 0 <= ix < row and 0 <= jy < len(grid[0]) and grid[ix][jy] == '1':
                    dfs(ix, jy)

        while r < row:
            while '1' not in grid[r]:
                r += 1
                if r >= row:
                    return nums

            c = grid[r].index('1')
            nums += 1
            dfs(r, c)

        return nums
# 执行结果：通过
# 执行用时 :80 ms, 在所有 Python3 提交中击败了100.00% 的用户
# 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了77.27%的用户


# 广度优先搜索BFS-队列
class Solution2:
    def numIslands(self, grid: list[list[str]]) -> int:
        nums = 0
        row = len(grid)
        r, q = 0, []

        while r < row:
            while '1' not in grid[r]:
                r += 1
                if r >= row:
                    return nums

            c = grid[r].index('1')
            nums += 1
            q.append((r, c))
            grid[r][c] = '0'
            while len(q) != 0:
                i, j = q.pop(0)
                # grid[i][j] = '0'
                # 按照上、下、左、右的顺序进行搜索
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ix = i + x
                    jy = j + y
                    if 0 <= ix < row and 0 <= jy < len(grid[0]) and grid[ix][jy] == '1':
                        q.append((ix, jy))
                        grid[ix][jy] = '0'

        return nums
# 执行结果：通过
# 执行用时 :72 ms, 在所有 Python3 提交中击败了100.00% 的用户
# 内存消耗 :13.6 MB, 在所有 Python3 提交中击败了98.18%的用户


class Solution22:
    def numIslands(self, grid: list[list[str]]) -> int:
        nums = 0
        row = len(grid)
        r = 0

        def bfs(i, j):
            q = [(i, j)]
            grid[r][c] = '0'
            while len(q) != 0:
                i, j = q.pop(0)
                # grid[i][j] = '0'
                # 按照上、下、左、右的顺序进行搜索
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ix = i + x
                    jy = j + y
                    if 0 <= ix < row and 0 <= jy < len(grid[0]) and grid[ix][jy] == '1':
                        q.append((ix, jy))
                        grid[ix][jy] = '0'

        while r < row:
            while '1' not in grid[r]:
                r += 1
                if r >= row:
                    return nums

            c = grid[r].index('1')
            nums += 1
            bfs(r, c)

        return nums
# 执行结果：通过
# 执行用时 :76 ms, 在所有 Python3 提交中击败了100.00% 的用户
# 内存消耗 :13.6 MB, 在所有 Python3 提交中击败了98.41%的用户


# 并查集
class Solution3:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    # f[r * col + c] = find(r * col + c)
                    print('rc: ', r, c, f)
                    # 按照右、下的顺序进行搜索
                    for x, y in [(0, 1), (1, 0)]:
                        rx = r + x
                        cy = c + y
                        if 0 <= rx < row and 0 <= cy < len(grid[0]) and grid[rx][cy] == '1':
                            union(rx * col + cy, r * col + c)
                            print(rx, cy, f)
        nums = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    nums.add(find(i * col + j))

        return len(nums)
# 执行结果：通过
# 执行用时 :96 ms, 在所有 Python3 提交中击败了100.00% 的用户
# 内存消耗 :16.4 MB, 在所有 Python3 提交中击败了11.59%的用户

'''
rc:  0 0 {0: 0}
0 1 {0: 0, 1: 0}
rc:  0 1 {0: 0, 1: 0}
0 2 {0: 0, 1: 0, 2: 0}
1 1 {0: 0, 1: 0, 2: 0, 4: 0}
rc:  0 2 {0: 0, 1: 0, 2: 0, 4: 0}
rc:  1 1 {0: 0, 1: 0, 2: 0, 4: 0}
2 1 {0: 0, 1: 0, 2: 0, 4: 0, 7: 0}
rc:  2 0 {0: 0, 1: 0, 2: 0, 4: 0, 7: 0, 6: 6}
2 1 {0: 6, 1: 0, 2: 0, 4: 0, 7: 0, 6: 6}
rc:  2 1 {0: 6, 1: 0, 2: 0, 4: 0, 7: 0, 6: 6}
2 2 {0: 6, 1: 0, 2: 0, 4: 0, 7: 0, 6: 6, 8: 0}
rc:  2 2 {0: 6, 1: 0, 2: 0, 4: 0, 7: 0, 6: 6, 8: 0}

'''

'''
rc:  0 0 {0: 0}
1 0 {0: 0, 5: 0}
rc:  0 2 {0: 0, 5: 0, 2: 2}
0 3 {0: 0, 5: 0, 2: 2, 3: 2}
1 2 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2}
rc:  0 3 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2}
0 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2}
rc:  0 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2}
1 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2}
rc:  1 0 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2}
2 0 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0}
rc:  1 2 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0}
2 2 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2}
rc:  1 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2}
2 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2, 14: 2}
rc:  2 0 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2, 14: 2}
2 1 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2, 14: 2, 11: 0}
rc:  2 1 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 2, 14: 2, 11: 0}
2 2 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 0, 14: 2, 11: 0}
rc:  2 2 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 0, 14: 2, 11: 0}
rc:  2 4 {0: 0, 5: 0, 2: 2, 3: 2, 7: 2, 4: 2, 9: 2, 10: 0, 12: 0, 14: 2, 11: 0}

'''
