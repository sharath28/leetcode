class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict = {}
        for num in nums:
            if num in temp_dict:
                return num
            else:
                temp_dict[num] = 1
