class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         count = 0
#         max_count = 0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 count += 1
#             elif nums[i] == 0:
#                 max_count = max(count,max_count)
#                 count = 0

#         return max(max_count,count)
        return max(map(len, ''.join(map(str, nums)).split('0')))
