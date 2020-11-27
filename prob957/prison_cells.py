class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        i = 1
        seen = {}
        flag = 0
        while N>0:
            N -= 1
            temp = []
            for j in range(8):
                if j == 0 or j == 7:
                    temp.append(0)
                else:
                    if (cells[j-1]==0 and cells[j+1]==0) or (cells[j-1]==1 and cells[j+1]==1):
                        temp.append(1)
                    else:
                        temp.append(0)
            dict_temp = tuple(temp)
            if dict_temp in seen and flag == 0:
                flag == 1
                N %= seen[dict_temp]-N
            else:
                seen[dict_temp] = N
            cells = temp

        return cells
