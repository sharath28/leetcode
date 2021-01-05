class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        index_dict = {}
        nums1 = sorted(nums,reverse = True)
        for i in range(len(nums1)):
            index_dict[nums1[i]] = i + 1
        return_list = []
        for num in nums:
            if index_dict[num] == 1:
                return_list.append("Gold Medal")
            elif index_dict[num] == 2:
                return_list.append("Silver Medal")
            elif index_dict[num] == 3:
                return_list.append("Bronze Medal")
            else:
                return_list.append(str(index_dict[num]))
        return return_list
