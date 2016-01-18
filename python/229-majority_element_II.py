# 在计算个数时使用便利的方法导致 judge 用了 500+ms，还没有想到优化方法。

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        result_list = list()
        if nums_len == 0:
            return []
        while True:
            current_num = nums[0]
            nums.pop(0)
            current_num_count = 1
            index = 0
            for i in range(len(nums)):
                if current_num == nums[index]:
                    nums.pop(index)
                    current_num_count += 1
                else:
                    index += 1
            if current_num_count > nums_len/3:
                result_list.append(current_num)
            if len(result_list)==2 or len(nums)==0:
                return result_list
