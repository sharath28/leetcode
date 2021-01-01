class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [False]*len(nums)
        res = 0
        for i in range(len(nums)):
            if visited[i] == False:
                start = nums[i]
                count = 0
                while True:
                    start = nums[start]
                    count += 1
                    visited[start] = True
                    if start == nums[i]:
                        break
                res = max(res,count)
        return res
