class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n = len(nums)
        # if n*k == 0:
        #     return []
        # return [max(nums[i:i+k]) for i in range(n-k+1)]
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums

        left = [0]*n
        left[0] = nums[0]
        right = [0]*n
        right[n-1] = nums[n-1]
        for i in range(1,n):
            if i%k==0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1],nums[i])

            j = n-i-1
            if (j+1)%k ==0:
                right[j] =nums[j]
            else:
                right[j] = max(right[j+1],nums[j])

        output = []
        for i in range(n-k+1):
            output.append(max(left[i+k-1],right[i]))
        return output


#         def clean_deque(i):
#             if deq and deq[0] == i-k:
#                 deq.popleft()

#             while deq and nums[i] > nums[deq[-1]]:
#                 deq.pop()

#         deq = deque()
#         max_idx = 0
#         for i in range(k):
#             clean_deque(i)
#             deq.append(i)
#             if nums[i] > nums[max_idx]:
#                 max_idx = i
#         output = [nums[max_idx]]

#         for i in range(k,n):
#             clean_deque(i)
#             deq.append(i)
#             output.append(nums[deq[0]])
#         return output
