# -*- coding:utf-8 -*-
# @time   : 2019-12-10 08:50
# @author : xulei
# @project: leetcode

'''
标签：简单、排序
题目：
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 
提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array

'''

class Solution1:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result, arr11 = [], []
        for i in arr1: #遍历arr1
            if i in arr2: #元素在arr2中存在
                if i in result: #若元素在结果数组中已经存在，找到元素在结果数组中的第一个位置，并把这个元素插入在前面的位置
                    i_index = result.index(i)
                    result.insert(i_index, i)
                else: #若元素在结果数组中不存在，则查看arr2数组中元素后面元素在arr2数组中是否存在，并找在arr2数组中第一个元素的位置
                    i_index_arr2 = arr2.index(i)
                    j_exist = False
                    for j in arr2[i_index_arr2:]:
                        if j in result:
                            j_index = result.index(j)
                            result.insert(j_index, i)
                            j_exist = True
                            break
                    if not j_exist:
                        result.append(i)
            else:
                arr11.append(i)

        if len(arr11) > 0:
            result.extend(sorted(arr11))

        return result

# 执行结果：通过
# 执行用时 :52 ms, 在所有 python3 提交中击败了75.79%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户

#把arr1中元素用字典提取出来，key为值，value为个数
class Solution2: #arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        kv, result = dict(), []
        for i in arr1:
            if i in kv.keys():
                kv[i] += 1
            else:
                kv[i] = 1
        for j in arr2:
            if j in kv.keys():
                result.extend([j]*kv[j])
                del kv[j]
        for k in sorted(kv.keys()):
            result.extend([k]*kv[k])

        return result

# 执行结果：通过
# 执行用时 :36 ms, 在所有 python3 提交中击败了99.21%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了100.00%的用户
