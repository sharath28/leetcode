class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
#         def check_increase(n):
#             temp_n = str(n)
#             for i in range(len(temp_n)-1):
#                 if temp_n[i]>temp_n[i+1]:
#                     return False
#             return True

#         while N>0:
#             if check_increase(N) == True:
#                 return N
#             N -= 1
#         return -1
        # digits = []
        # A = map(int,str(N))
        # for i in xrange(len(A)):
        #     for d in xrange(1,10):
        #         if digits + [d] * (len(A)-i) > A:
        #             digits.append(d-1)
        #             break
        #     else:
        #         digits.append(9)
        # return int("".join(map(str,digits)))
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1])-1)
            i -= 1
        S[i+1:] = '9'*(len(S)-i-1)
        return int("".join(S))

                    
