class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        flag = 0
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                temp = nums_dict[nums[i]]
                flag = 1
                if abs(temp-i)<=k:
                    return True
                nums_dict[nums[i]] = i
        return False
