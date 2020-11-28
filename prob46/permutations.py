class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i]=nums[i],nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
