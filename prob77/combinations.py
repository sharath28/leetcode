class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
#################3
#Backtracking
#         def backtrack(first=1,curr=[]):
#             if len(curr)==k:
#                 output.append(curr[:])
#             for i in range(first,n+1):
#                 curr.append(i)
#                 backtrack(i+1,curr)
#                 curr.pop()

#         output = []
#         backtrack()
#         return output
##############
#Lexicographic (binary sorted) combinations
        nums = list(range(1,k+1))+[n+1]

        output, j = [],0
        while j<k:
            output.append(nums[:k])
            j=0
            while j<k and nums[j+1]==nums[j]+1:
                nums[j]=j+1
                j += 1
            nums[j] += 1
        return output
