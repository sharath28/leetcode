class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp_dict = {}
        for i in range(len(nums)):
            if nums[i] not in temp_dict:
                temp_dict[nums[i]]=1
            else:
                duplicate = nums[i]
        for i in range(len(nums)):
            if i+1 not in temp_dict:
                not_found = i+1
        return [duplicate,not_found]
