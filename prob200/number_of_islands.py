class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def get_islands_count(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return 0

            grid[i][j] = '0'
            get_islands_count(grid,i-1,j)
            get_islands_count(grid,i+1,j)
            get_islands_count(grid,i,j-1)
            get_islands_count(grid,i,j+1)

            return 1

        if grid is None or len(grid)==0:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_islands += get_islands_count(grid,i,j)

        return num_islands
