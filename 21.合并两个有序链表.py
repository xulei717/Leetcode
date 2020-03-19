# -- coding:utf-8 --
# @time : 2020-3-2 20:53
# @author : xulei
# @project: leetcode


"""
标签：简单、栈、字符串
题目：将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll = ListNode(0)
        p, q, t = l1, l2, ll
        while p is not None and q is not None:
            if p.val <= q.val:
                t.next = ListNode(p.val)
                p = p.next
                t = t.next
            else:
                t.next = ListNode(q.val)
                q = q.next
                t = t.next
            print(ll)
        if p is not None:
            t.next = p
        if q is not None:
            t.next = q
        return ll.next
#执行结果：通过
#执行用时 :180 m, 在所有 Python3 提交中击败了6.81%的用户
#内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.21%的用户


