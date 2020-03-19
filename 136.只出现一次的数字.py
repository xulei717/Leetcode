# -- coding:utf-8 --
# @time : 2020-3-17 13:06
# @author : xulei
# @project: leetcode


"""
标签：简单、位运算、哈希表
题目：给定一个二叉树，找出其最大深度。

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 排序后，按照相邻位置数值是否一致，判断唯一值
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        #print(ns)
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]
# 时间复杂度：nlogn(sort-快排)+n=nlogn ； 空间复杂度：1
# 执行结果：通过
# 执行用时 :64 ms, 在所有 Python3 提交中击败了78.15%的用户
# 内存消耗 :15.1 MB, 在所有 Python3 提交中击败了51.07%的用户

# 位运算
'''
如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
a⊕0=a
如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
a⊕a=0
XOR 满足交换律和结合律
a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

作者：LeetCode
链接：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
# 时间复杂度：n-遍历一遍元素 ； 空间复杂度：1
# 执行结果：通过
# 执行用时 :64 ms, 在所有 Python3 提交中击败了78.15%的用户
# 内存消耗 :15.1 MB, 在所有 Python3 提交中击败了72.09%的用户
