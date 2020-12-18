class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        ans = ""
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch,1])
            if stack[-1][1] == k:
                stack.pop()

        for ele in stack:
            ans += ele[0]*ele[1]
        return ans
            
