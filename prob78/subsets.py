from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # i = 0
        # output_list = []
        # while i < len(nums)+1:
        #     for temp in combinations(nums,i):
        #         output_list.append(list(temp))
        #     i += 1
        # return output_list
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output
