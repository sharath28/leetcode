class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_id = -1
        for i in range(len(nums)):
            if nums[i]==target:
                left_id = i
                break
        if left_id == -1:
            return [-1,-1]

        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                right_id = j
                break
        return [left_id,right_id]


        low = 0, high = len(nums)-1
        flag = 0
        while low<high:
            mid = low + (high-low)/2
            if nums[mid] == target and nums[mid-1]!=target:
                flag = 1
            if nums[mid]>target:
                high = mid-1
            else:
                low = mid + 1
