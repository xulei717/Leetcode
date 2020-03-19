# -- coding:utf-8 --
# @time : 2020-3-16 12:25
# @author : xulei
# @project: leetcode


"""
标签：简单、树、深度优先搜索
题目：给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 队列 + 层次遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [root]
        i = 0
        while len(res) > 0:
            # print(i, len(res), res)
            n = len(res)
            i += 1
            for k in range(n):
                tp = res.pop(0)
                if tp.left:
                    res.append(tp.left)
                if tp.right:
                    res.append(tp.right)

        return i

# 执行结果：通过
# 执行用时 :52 ms, 在所有 Python3 提交中击败了44.07%的用户
# 内存消耗 :14.7 MB, 在所有 Python3 提交中击败了13.38%的用户