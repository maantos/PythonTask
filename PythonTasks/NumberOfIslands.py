#DFS Solution
class Solution(object):
    def numIslands(self, grid):
        if grid is None or len(grid) is 0:
            return 0

        count = 0
        rows = len(grid)
        columns = len(grid[0])

        coordinats = [[1,0],[0,1],[-1,0],[0,-1]]

        stack = []
        def dfs(grid, i, j):
            if 0 <= i < rows and 0 <= j < columns and grid[i][j] == '1':
                grid[i][j] = '2'
                for d in coordinats:
                    dfs(grid, i+d[0] , j+d[1])
                return 1

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    count += dfs(grid, i,j)
        return count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))
