#BFS Solution
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        if grid is None or len(grid) is 0:
            return 0

        count = 0
        rows = len(grid)
        columns = len(grid[0])

        coordinats = [[1,0],[0,1],[-1,0],[0,-1]]

        que = deque()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    count += 1
                    que.append([i,j])
                    grid[i][j] = '2'
                    while que:
                        x,y = que.popleft()
                        for d in coordinats:
                            r = x + d[0]
                            c = y + d[1]
                            if 0 <= r < rows and 0 <= c < columns and grid[r][c] == '1':
                                que.append([r,c])
                                grid[r][c] = '2'

        return count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))
