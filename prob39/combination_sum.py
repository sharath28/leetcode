class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(remain, first=0,curr=[]):
            if sum(curr)==target:
                output.append(curr[:])
                return
            elif remain < 0:
                return
            for i in range(first,len(candidates)):
                curr.append(candidates[i])
                backtrack(remain-candidates[i], i,curr)
                curr.pop()

        output = []
        backtrack(target,0,[])
        return output
