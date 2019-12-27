# -*- coding:utf-8 -*-
# @time   : 2019-12-12 08:52
# @author : xulei
# @project: leetcode


"""
标签：简单、排序、树
题目：
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归-栈
'''
两个树互为镜像成立的条件：
1.两个树的根节点具有相同的值
2.每个树的右子树与另一个树的左子树镜像对称
'''
class Solution1:
    def isMissor(self, t1:TreeNode, t2:TreeNode):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.isMissor(t1.left, t2.right) and self.isMissor(t1.right, t2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMissor(root, root)

# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了96.01%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.45%的用户
'''
复杂度分析
时间复杂度：O(n)O(n)，因为我们遍历整个输入树一次，所以总的运行时间为 O(n)O(n)，其中 nn 是树中结点的总数。
空间复杂度：递归调用的次数受树的高度限制。在最糟糕情况下，树是线性的，其高度为 O(n)O(n)。因此，在最糟糕的情况下，由栈上的递归调用造成的空间复杂度为 O(n)O(n)。
'''

#迭代-队列
'''
队列中两个连续的结点应该是相等的，而且它们的子树互为镜像。
最初，队列中包含的是root和root。
每次提取两个结点并比较它们的值，然后将两个结点的左右子结点按相反的顺序插入到队列中。
当队列为空，或者检测到两个连续结点不相等时，算法结束。
'''
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        lt = [root, root]
        while len(lt) > 0:
            t1 = lt.pop()
            t2 = lt.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            lt.extend([t1.left, t2.right, t1.right, t2.left])

        return True

# 执行结果：通过
# 执行用时 :32 ms, 在所有 python3 提交中击败了98.79%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.45%的用户
'''
复杂度分析
时间复杂度：O(n)O(n)，因为我们遍历整个输入树一次，所以总的运行时间为 O(n)O(n)，其中 nn 是树中结点的总数。
空间复杂度：搜索队列需要额外的空间。在最糟糕情况下，我们不得不向队列中插入 O(n)O(n) 个结点。因此，空间复杂度为 O(n)O(n)。
'''
