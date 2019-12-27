# -*- coding:utf-8 -*-
# @time   : 2019-12-11 08:51
# @author : xulei
# @project: leetcode


'''
标签：简单、树
题目：
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#广度优先遍历-->队列：先进先出，非递归
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        else:
            if q is None:
                return False

        lp, lq = [p.val, p.left, p.right], [q.val, q.left, q.right]
        i, j = 1, 1
        while i < len(lp):
            while i < len(lp) and not isinstance(lp[i], TreeNode):
                i += 1
            if i < len(lp):
                p = lp[i]
                # del lp[i] #删除TreeNode类型的节点，相同的值，但是标识符不一样
                lp[i] = p.val
                # lp.append(p.val)
                lp.append(p.left)
                lp.append(p.right)
                # i += 1

        while j < len(lq):
            while j < len(lq) and not isinstance(lq[j], TreeNode):
                j += 1
            if j < len(lq):
                q = lq[j]
                lq[j] = q.val
                # lq.append(q.val)
                lq.append(q.left)
                lq.append(q.right)
                # j += 1

        print(lp)
        print(lq)
        if lp == lq:
            return True

        return False

# 执行结果：通过
# 执行用时 :28 ms, 在所有 python3 提交中击败了98.95%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.09%的用户

#深度优先遍历-->栈：先进后出，递归
#终止条件与返回值：
#当两个节点都会空时，返回True；
#当两个节点，一个为空，一个不为空，则返回False；
#当两个节点都不会空，但是值不相等时，则返回False
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 复杂度分析
# 时间复杂度 : O(N)O(N)，其中 N 是树的结点数，因为每个结点都访问一次。
# 空间复杂度 : 最优情况（完全平衡二叉树）时为 O(\log(N))O(log(N))，最坏情况下（完全不平衡二叉树）时为 {O}(N)O(N)，用于维护递归栈。

# 执行结果：通过
# 执行用时 :28 ms, 在所有 python3 提交中击败了98.95%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.48%的用户


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    print(p.left)
    print(p.left.left)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.right = TreeNode(4)

    # p, q = None, None

    s1 = Solution1()
    print(s1.isSameTree(p, q))
