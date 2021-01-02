class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # global_inversion = 0
        # local_inversion = 0
        # for i in range(len(A)-1):
        #     if A[i]>A[i+1]:
        #         local_inversion += 1
        # for i in range(len(A)-1):
        #     # print(i)
        #     for j in range(i+1,len(A)):
        #         if A[i]>A[j]:
        #             global_inversion += 1
        # if global_inversion == local_inversion:
        #     return True
        # else:
        #     return False
        # n = len(A)
        # floor = n
        # for i in xrange(n-1,-1,-1):
        #     floor = min(floor,A[i])
        #     if i >=2 and A[i-2] > floor:
        #         return False
        # return True
        return all(abs(i-x) <= 1 for i,x in enumerate(A))
