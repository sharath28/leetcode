class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = {}
        queue = []
        visited = [False]*len(s)
        queue.append(0)
        while len(queue)>0:
            start = queue.pop()
            if visited[start] == False:
                for end in range(start+1,len(s)+1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited[start] = True
        return False


        # for word in wordDict:
        #     word_dict[word] = 1
        # memo = [False]*len(s)
        # return self.wordBreak1(s,word_dict,0,memo)

    # def wordBreak1(self, s, word_dict, start,memo):
    #     if start == len(s):
    #         # print(start,len(s))
    #         return True
    #     if memo[start]!=False:
    #         return memo[start]
    #     for end in range(start+1,len(s)+1):
    #         # print(s[start:end])
    #         if (s[start:end] in word_dict) and self.wordBreak1(s,word_dict,end,memo):
    #             memo[start] = True
    #             return memo[start]
    #     memo[start] = False
    #     return memo[start]
