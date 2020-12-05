class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = list(nums)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original
        self.original = list(self.original)
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
#         aux = list(self.nums)

#         for idx in range(len(self.nums)):
#             remove_idx = random.randrange(len(aux))
#             self.nums[idx] = aux.pop(remove_idx)

        for i in range(len(self.nums)):
            swap_idx = random.randrange(i,len(self.nums))
            self.nums[i],self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
