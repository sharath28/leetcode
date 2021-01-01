class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # a = int(''.join(map(str,A)))
        # temp_sum = a+K
        # temp_list = list(str(temp_sum))
        # temp_list = map(int,temp_list)
        # return temp_list
        A[-1] += K
        for i in xrange(len(A)-1,-1,-1):
            carry,A[i] = divmod(A[i],10)
            if i:
                A[i-1] += carry
        if carry:
            A = map(int,str(carry)) + A
        return A
