class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        prevMax = 0
        for num in nums:
            temp = currMax
            if prevMax + num > currMax:
                currMax = prevMax + num
            else:
                currMax = currMax
            prevMax = temp
        return currMax
