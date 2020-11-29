class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#         lastNonZero = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[lastNonZero] = nums[i]
#                 lastNonZero += 1

#         for j in range(lastNonZero,len(nums)):
#             nums[j]=0

        lastNonZero = 0
        curr = 0
        while curr <len(nums):
            print(nums,curr,lastNonZero)
            if nums[curr]!=0:
                temp = nums[lastNonZero]
                nums[lastNonZero] = nums[curr]
                nums[curr] = temp
                lastNonZero += 1
            curr += 1
        # i = 0
        # j = len(nums)-1
        # count = 0
        # while i<len(nums)-count-1:
        #     print(nums)
        #     if nums[i]==0:
        #         for k in range(i,len(nums)-1):
        #             nums[k]=nums[k+1]
        #         nums[len(nums)-1]=0
        #         count += 1
        #     else:
        #         i += 1
#         numZeros = 0
#         for num in nums:
#             if num == 0:
#                 numZeros += 1
#         result = []
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 result.append(nums[i])

#         while numZeros>0:
#             result.append(0)
#             numZeros -= 1

#         for i in range(len(nums)):
#             nums[i] = result[i]


        
