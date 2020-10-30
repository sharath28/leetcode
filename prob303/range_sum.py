class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.list[i:j+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
