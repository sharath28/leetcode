class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        temp_dict = {}
        for i in range(len(arr)):
            temp_dict[arr[i]] = i

        for i in range(len(arr)):
            if 2*arr[i] in temp_dict:
                if temp_dict[2*arr[i]] != i:
                    return True
        return False
