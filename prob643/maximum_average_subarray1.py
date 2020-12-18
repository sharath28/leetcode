class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # max_average = -999999999999
        # if len(nums)<=k:
        #     return sum(nums)/float(len(nums))
        # for i in range(len(nums)-k+1):
        #     temp_sum = sum(nums[i:i+k])
        #     average = temp_sum/float(k)
        #     if average>max_average:
        #         max_average = average
        # return max_average
        sums = [0]*len(nums)
        sums[0] = nums[0]
        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]
        res = (sums[k-1]*1.0)/k
        for i in range(k,len(nums)):
            res = max(res,(sums[i]-sums[i-k])*1.0/k)
        return res
            
