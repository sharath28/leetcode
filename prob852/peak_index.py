class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ##############
        #Linear check
        # i = 0
        # while arr[i]<arr[i+1]:
        #     i+= 1
        # return i
        #############
        #Binary Search
        low = 0
        high = len(arr)-1
        while low<high:
            pivot = low +(high-low)/2
            if arr[pivot]<arr[pivot+1]:
                low = pivot+1
            else:
                high = pivot
        return low
