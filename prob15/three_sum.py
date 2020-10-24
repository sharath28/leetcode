from itertools import permutations
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #######################
        #Time Limit Exceeded
        # if len(nums)<3:
        #     return []
        # return_list = []
        # temp_dict = {}
        # for combination in combinations(nums,3):
        #     if sum(combination) == 0:
        #         val = tuple(sorted(combination))
        #         if val not in temp_dict:
        #             temp_dict[val]=1
        #             return_list.append(list(combination))
        #         else:
        #             continue
        # print(temp_dict)
        # return return_list
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i == 0 or nums[i-1]!=nums[i]:
                self.two_sum(nums,i,res)
        return res

    def two_sum(self,nums,i,res):
        seen = set()
        j = i+1
        while j < len(nums):
            complement = -nums[i]-nums[j]
            if complement in seen:
                res.append([nums[i],nums[j],complement])
                while j+1<len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1
    
