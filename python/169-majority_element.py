# 题目上标了 Divide and Conquer 的标签，但是还是用遍历的方法解决的，没有想到分而治之的方法。
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_num = len(nums)
        num_count = dict()
        for i in nums:
            if i in num_count.keys():
                num_count[i] += 1
            else:
                num_count[i] = 1
        for k,v in num_count.items():
            if v > nums_num/2:
                return k
