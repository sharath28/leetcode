class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def find_slope(x1,x2,y1,y2):
            if x2-x1 == 0:
                return -1
            else:
                return (y2-y1)/float((x2-x1))

        # if coordinates[1][0]-coordinates[0][0] == 0:
        #     slope = coordinates[1][1]-coordinates[0][1]
        # else:
        #     slope = (coordinates[1][1]-coordinates[0][1])/float((coordinates[1][0]-coordinates[0][0]))
        # for i in range(2,len(coordinates)):
        #     if coordinates[i][0]-coordinates[i-1][0] == 0:
        #         if coordinates[i][1]-coordinates[i-1][1] != slope:
        #             return False
        #     elif (coordinates[i][1]-coordinates[i-1][1])/float((coordinates[i][0]-coordinates[i-1][0])) != slope:
        #         return False
        # return True
        slope = find_slope(coordinates[0][0],coordinates[1][0],coordinates[0][1],coordinates[1][1])
        # print(slope)

        c = 1
        i = 1
        p = coordinates
        while i < len(p)-1:
            temp_slope = find_slope(p[i][0], p[i+1][0], p[i][1], p[i+1][1])
            # print(temp_slope)
            if temp_slope != slope:
                c = 0
                break
            i+=1

        if c == 1:
            return True
        else:
            return False
