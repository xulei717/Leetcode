# -*- coding:utf-8 -*-
# @time   : 2020-01-21 10:27
# @author : xl
# @project: leetcode

"""
标签：困难、堆、链表、分治算法
题目：
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 堆排序，顶点都是最小值
import heapq
class Solution:
    def mergeKLists(self, lists):
        if not lists: return None
        heap = []
        for ll in lists:
            while ll is not None:
                heapq.heappush(heap, ll.val)
                ll = ll.next
        print('heap: ', heap)
        head = None
        if len(heap) != 0:
            head = ListNode(heapq.heappop(heap))
            print('head: ', head)
            tm = head
            while heap:
                temp = ListNode(heapq.heappop(heap))
                tm.next = temp
                tm = temp
                # print(head)
        return head
# 执行结果：通过
# 执行用时 :100 ms, 在所有 Python3 提交中击败了93.25% 的用户
# 内存消耗 :17.1 MB, 在所有 Python3 提交中击败了46.91%的用户


# 排序
class Solution1:
    def mergeKLists(self, lists):
        if not lists: return None
        nodes = []
        for ll in lists:
            while ll is not None:
                nodes.append(ll.val)
                ll = ll.next
        print('nodes: ', nodes)
        head = None
        if len(nodes) != 0:
            nodes_sort = sorted(nodes)
            head = ListNode(nodes_sort[0])
            nodes_sort = nodes_sort[1:]
            print('head: ', head)
            tm = head
            while nodes_sort:
                temp = ListNode(nodes_sort[0])
                nodes_sort = nodes_sort[1:]
                tm.next = temp
                tm = temp
                # print(head)
        return head

# 执行结果：通过
# 执行用时 :284 ms, 在所有 Python3 提交中击败了18.30% 的用户
# 内存消耗 :17 MB, 在所有 Python3 提交中击败了58.80%的用户


# 逐一比较：优先队列（堆）????????????????????????????????????
# 比较K个节点（每个链表的首节点），获得最小值的节点
# 将选中的节点接在最终有序链表的后面
from queue import PriorityQueue
class Solution2:
    def mergeKLists(self, lists):
        if not lists: return None
        head = point = ListNode(0)
        q = PriorityQueue()
        for ll in range(len(lists)):
            if lists[ll]:
                q.put((lists[ll].val, ll))
                lists[ll] = lists[ll].next
                print(lists[ll])
        print(q.queue)
        while q:
            val, node_index = q.get()
            print(val, node_index)
            point.next = ListNode(val)
            point = point.next

            if lists[node_index]:
                q.put((lists[node_index].val, node_index))
                lists[node_index] = lists[node_index].next
            print(q.queue)
            print(head.next)
        return head.next


import heapq
class Solution3:
    def mergeKLists(self, lists):
        if not lists: return None
        head = point = ListNode(0)
        q = []
        for ll in range(len(lists)):
            if lists[ll]:
                heapq.heappush(q, (lists[ll].val, ll))
                lists[ll] = lists[ll].next
                print(lists[ll])
        print(q)
        while q:
            val, node_index = heapq.heappop(q)
            print(val, node_index)
            point.next = ListNode(val)
            point = point.next

            if lists[node_index]:
                heapq.heappush(q, (lists[node_index].val, node_index))
                lists[node_index] = lists[node_index].next
            print(q)
            print(head.next)
        return head.next
# 执行结果：通过
# 执行用时 :124 ms, 在所有 Python3 提交中击败了68.84% 的用户
# 内存消耗 :16.8 MB, 在所有 Python3 提交中击败了65.57%的用户


# 分治算法-分而治之-递归
class Solution4:
    def mergeKLists(self, lists):
        if not lists: return None
        n = len(lists)
        return self.merge(lists, 0, n-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right-left)//2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
# 执行结果：通过
# 执行用时 :132 ms, 在所有 Python3 提交中击败了60.57% 的用户
# 内存消耗 :22.9 MB, 在所有 Python3 提交中击败了9.47%的用户
