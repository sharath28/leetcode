class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final_list = []
        final_list.append(nums[0])
        for i in range(1,len(nums)):
            final_list.append(nums[i]+final_list[i-1])
        return final_list
