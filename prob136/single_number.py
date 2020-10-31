class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)>0:
            num = nums[0]
            nums.remove(num)
            if num not in nums:
                return num
            else:
                nums.remove(num)
