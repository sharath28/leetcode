class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        temp_arr1 = {}
        temp_arr2 = {}
        temp_arr3 = {}


        for num in arr1:
            temp_arr1[num] = 1
        for num in arr2:
            temp_arr2[num] = 1
        for num in arr3:
            temp_arr3[num] = 1

        result = []
        for num in temp_arr1:
            if num in temp_arr2 and num in temp_arr3:
                result.append(num)
        return sorted(result)
