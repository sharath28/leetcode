class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        high = max(nums)
        temp = {}
        for num in nums:
            temp[num]=1
        for i in range(1,len(nums)+1):
            if i not in temp:
                return i
        return high+1
