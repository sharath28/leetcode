def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        j = i+1
        while j != len(nums):
            if nums[i] + nums[j] == target:
                return [i,j]
            j = j +1

if __name__ == '__main__':
    print(twoSum([2,7,11,15],9))