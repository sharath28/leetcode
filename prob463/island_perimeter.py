class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
#                 if grid[r][c] == 1:
#                     if r == 0:
#                         up = 0
#                     else:
#                         up = grid[r-1][c]
#                     if c == 0:
#                         left = 0
#                     else:
#                         left = grid[r][c-1]
#                     if r == rows-1:
#                         down = 0
#                     else:
#                         down = grid[r+1][c]
#                     if c == cols-1:
#                         right = 0
#                     else:
#                         right = grid[r][c+1]

#                     result += 4-(up+left+right+down)
                if grid[r][c] == 1:
                    result += 4

                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2

                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2

        return result
