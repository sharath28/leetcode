class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ###################
        #O(n^2)
        # final_list = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i]>nums[j]:
        #             count += 1
        #     final_list.append(count)
        # return final_list
        ###################
        #O(n)
        d={}
        for num,value in enumerate(sorted(nums)):
            print(num,value)
            if value not in d:
                d[value]=num
        return [d[num] for num in nums]
