class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(arr)):
            j = i + 1
            while j <= len(arr):
                total += sum(arr[i:j])
                j += 2
        return total
