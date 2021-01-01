class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        temp_dict = {}
        for i in range(len(B)):
            temp_dict[B[i]] = i

        return_list = []
        for num in A:
            return_list.append(temp_dict[num])
        return return_list
