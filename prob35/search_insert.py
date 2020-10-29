class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <=right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            if target<nums[pivot]:
                right = pivot-1
            else:
                left = pivot+1
        return left
        
