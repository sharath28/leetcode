class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         temp_dict = {}
#         for num in nums:
#             temp_dict[num] = 1

#         return_list = []
#         for i in range(1,len(nums)+1):
#             if i not in temp_dict:
#                 return_list.append(i)
#         return return_list
        for i in range(len(nums)):
            new_index = abs(nums[i])-1
            if nums[new_index]>0:
                nums[new_index] *= -1

        return_list = []
        for i in range(1,len(nums)+1):
            if nums[i-1]>0:
                return_list.append(i)
        return return_list
