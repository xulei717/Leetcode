# -*- coding:utf-8 -*-
# @time   : 2019-12-10 10:20
# @author : xulei
# @project: leetcode

'''
标签：中等、排序
题目：
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

示例 1：
输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：
输入：[1,1,1,1,2,2,3,3] -> [1,2,1,2,1,3,1,3]
输出：[1,3,1,3,2,1,2,1] -> [1,2,1,2,1,3,1,3]
                              [1,2,2,2,3,3] -> [1,2,3,2,3,2] -> [2,3,2,3,2,1] -> [2,3,1,2,3,2]
提示：
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distant-barcodes

'''

class Solution1:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        kv = dict() #统计list中每个元素出现的次数
        for i in set(barcodes):
            kv[i] = barcodes.count(i)

        rs = [] #按照元素出现的次数逆序统计元素
        for i in sorted(kv.values(), reverse=True):
            for j in kv.keys():
                if kv[j] == i:
                    rs.append(j)

        result = [rs[0]] * kv[rs[0]] #把最多的元素首先全放在结果列表里面
        vv = [] #统计出除了最多元素剩余元素按照逆序和元素个数放在一个列表里面
        for r in rs[1:]:
            vv = vv + [r] * kv[r]

        st, et, ll = 1, 1, 0
        for v in vv: #把剩余元素按照和最多元素一样的个数穿插到列表中
            if ll == kv[rs[0]]:
                st += 1
                et = st
                ll = 0
            result.insert(et, v)
            et += 2
            ll += 1

        return result

# 执行结果：超出时间限制

import collections

class Solution2:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        kv = dict(collections.Counter(barcodes)) #优化的地方
        print(kv)
        # 按照出现次数排序元素
        kv_sorted = sorted(kv, key=lambda x: -kv[x]) #优化的地方
        print(kv_sorted)
        # 重排序
        rsort = []
        for i in kv_sorted:
            rsort += [i] * kv[i]
        print(rsort)
        # 间隔插入 -- 优化的地方
        result = [0] * len(barcodes)
        result[::2] = rsort[:len(result[::2])]
        result[1::2] = rsort[len(result[::2]):]
        print(result)

        return result

# 执行结果：通过
# 执行用时 :480 ms, 在所有 python3 提交中击败了86.11%的用户
# 内存消耗 :14.7 MB, 在所有 python3 提交中击败了100.00%的用户

