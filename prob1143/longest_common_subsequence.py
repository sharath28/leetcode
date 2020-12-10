class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        # for col in reversed(range(len(text2))):
        #     for row in reversed(range(len(text1))):
        #         if text2[col] == text1[row]:
        #             dp[row][col] = 1+dp[row+1][col+1]
        #         else:
        #             dp[row][col] = max(dp[row+1][col],dp[row][col+1])
        # return dp[0][0]
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        prev = [0]*(len(text1)+1)
        curr = [0]*(len(text1)+1)

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    curr[row] = 1 + prev[row+1]
                else:
                    curr[row] = max(prev[row],curr[row+1])
            prev, curr = curr, prev
        return prev[0]
