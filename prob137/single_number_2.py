from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp_dict = defaultdict(int)
        for num in nums:
            temp_dict[num] += 1
        for num in temp_dict:
            if temp_dict[num] == 1:
                return num
