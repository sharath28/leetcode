class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        for i in range(len(numbers)):
            index_dict[numbers[i]]=i
        for i in range(len(numbers)):
            if target-numbers[i] in index_dict:
                return [i+1,index_dict[target-numbers[i]]+1]
