# 二分查找，这题应该归为 easy
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end_index = len(nums)-1
        start_index = 0
        while True:
            if start_index > len(nums)-1:
                return len(nums)
            if end_index < 0:
                return 0
            if start_index > end_index:
                return start_index
            index = (start_index + end_index)/2
            if nums[index] == target:
                return index
            if nums[index] > target:
                end_index = index-1
            else:
                start_index = index+1
