class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        y = lambda x: (a*x*x)+(b*x)+c
        final_list = []
        for num in nums:
            final_list.append(y(num))
        return sorted(final_list)
