class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        final_str = ''
        while k <= n:
            final_str += '{0:b}'.format(k)
            k += 1
        return int(final_str,2)%(pow(10,9)+7)
            
