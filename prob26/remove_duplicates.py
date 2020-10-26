class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = {}
        # i = 0
        # n = len(nums)
        # while i<n:
        #     if nums[i] in temp:
        #         nums[i]=nums[n-1]
        #         n-=1
        #     else:
        #         temp[nums[i]]=1
        #         i+=1
        # return n

        #Two pointers approach
        # if len(nums)==0:
        #     return 0
        # i = 0
        # for j in range(1,len(nums)):
        #     print(nums)
        #     if nums[j]!=nums[i]:
        #         i+=1
        #         nums[i]=nums[j]
        # return i+1

        if len(nums)==0:
            return 0
        i = 0
        j = 1
        n = len(nums)
        while j < n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1
