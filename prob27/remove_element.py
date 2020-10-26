class Solution(object):
    def move_to_last(self,nums,index):
        # print(index)
        temp = nums[index]
        for i in range(index,len(nums)-1):
            nums[i]=nums[i+1]
        nums[len(nums)-1]=temp
        # print(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Two pointers
        # i = 0
        # for j in range(len(nums)):
        #     print(nums)
        #     if nums[j] != val:
        #         nums[i]=nums[j]
        #         i+=1
        # return i

        #Swap value which matches
        i = 0
        n = len(nums)
        while i<n:
            # print(i)
            if nums[i]==val:
                nums[i]=nums[n-1]
                n-=1
            else:
                i+=1
            # print(nums)
        return n


        #Brute Force
        # count = 0
        # i = 0
        # while count+i<len(nums):
        #     # print(count+i)
        #     # print(nums)
        #     if nums[i]==val:
        #         count = count + 1
        #         self.move_to_last(nums,i)
        #         continue
        #     i=i+1
        # return len(nums)-count
