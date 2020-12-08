class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
#         stack = [0]

#         for x in S:
#             if x == '(':
#                 stack.append(0)
#             else:
#                 v = stack.pop()
#                 stack[-1] += max(2*v,1)

#         return stack.pop()

        ans = bal = 0
        for i,x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans
