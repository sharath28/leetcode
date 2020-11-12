class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k >0:
            last = nums.pop(len(nums)-1)
            nums.insert(0,last)
            k=k-1
