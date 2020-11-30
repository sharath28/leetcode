class Leaderboard(object):

    def __init__(self):
        self.player_dict = {}



    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.player_dict:
            self.player_dict[playerId] = score
        else:
            self.player_dict[playerId] += score


    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        temp_dict = sorted(self.player_dict.items(), key=lambda x: x[1], reverse= True)
        return_val = 0
        for i in range(K):
            return_val += temp_dict[i][1]
        return return_val




    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.player_dict[playerId]



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
