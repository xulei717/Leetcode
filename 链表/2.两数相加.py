# -*- coding:utf-8 -*-
# @time   : 2019-12-17 08:46
# @author : xulei
# @project: leetcode

"""
标签：中等、腾讯精选练习（50题）、链表、数学
题目：
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 每位相加，有进位就加前面位上或者多出一位
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll, ad = ListNode(0), 0
        result = ll
        while l1 is not None or l2 is not None:
            val = ll.val
            if l1 is not None:
                if l2 is not None:
                    val += l1.val + l2.val
                    l1 = l1.next
                    l2 = l2.next
                else:
                    val += l1.val
                    l1 = l1.next
            else:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                ll.val = val % 10
                ad = val // 10
            else:
                ll.val = val
                ad = 0
            if l1 is not None or l2 is not None:
                ll.next = ListNode(ad)
                ll = ll.next
            print(val, ad, ll)
        if ad != 0:
            ll.next = ListNode(ad)

        print(result)
        return result
# 执行结果：通过
# 执行用时 :108 ms, 在所有 python3 提交中击败了16.73%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.59%


# 用空间换时间，多生成局部变量，节省运算时间
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        lr, ad = result, 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                x = l1.val
            else:
                x = 0
            if l2 is not None:
                y = l2.val
            else:
                y = 0

            val = ad + x + y
            ad = val // 10
            lr.val = val % 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is not None or l2 is not None:
                lr.next = ListNode(0)
                lr = lr.next

        if ad != 0:
            lr.next = ListNode(ad)
            # lr = lr.next  # 最后的进位，next应该None
        return result
# 执行结果：通过
# 执行用时 :72 ms, 在所有 python3 提交中击败了92.99%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.59%

class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)  # 预先指针，指向头结点
        lr, ad = result, 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                x = l1.val
            else:
                x = 0
            if l2 is not None:
                y = l2.val
            else:
                y = 0

            val = ad + x + y
            ad = val // 10
            lr.next = ListNode(val % 10)
            lr = lr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if ad != 0:
            lr.next = ListNode(ad)
            # lr = lr.next  # 最后的进位，next应该None
        return result.next
# 执行结果：通过
# 执行用时 :72 ms, 在所有 python3 提交中击败了92.99%的用户
# 内存消耗 :12.6 MB, 在所有 python3 提交中击败了99.59%



