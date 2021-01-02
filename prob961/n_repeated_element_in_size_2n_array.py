class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)//2
        temp_dict = {}
        for num in A:
            if num not in temp_dict:
                temp_dict[num] = 1
            else:
                temp_dict[num] += 1
                if temp_dict[num] == n:
                    return num
