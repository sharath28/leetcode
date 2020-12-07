class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(list(map(lambda x:x*x,A)))
        n = len(A)
        j = 0

        while j < n and A[j] < 0:
            j += 1
        i = j - 1
        ans = []
        while 0 <= i and j<n:
            i_2 = A[i]**2
            j_2 = A[j]**2
            if i_2 < j_2:
                ans.append(i_2)
                i -= 1
            else:
                ans.append(j_2)
                j += 1

        while i>=0:
            ans.append(A[i]**2)
            i -= 1
        while j<n:
            ans.append(A[j]**2)
            j += 1

        return ans
