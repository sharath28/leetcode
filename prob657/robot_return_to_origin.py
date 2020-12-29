class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        temp_dict = {'L':(-1,0),'U':(0,1),'D':(0,-1),'R':(1,0)}
        coor = [0,0]
        for ch in moves:
            # print(temp_dict[ch])
            coor[0] += temp_dict[ch][0]
            coor[1] += temp_dict[ch][1]
        if coor == [0,0]:
            return True
        else:
            return False
