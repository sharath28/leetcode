class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        final_list = [[1],[1,1]]
        i = 2
        while i < numRows:
            temp = []
            for j in range(i+1):
                if j == 0:
                    temp.append(1)
                elif j == i:
                    temp.append(1)
                else:
                    temp.append(final_list[i-1][j-1]+final_list[i-1][j])
            final_list.append(temp)
            i = i + 1
        return final_list
