from collections import deque

mark = {}

class Solution:

    def bfs(self, grid, sx, sy):
        x = len(grid)
        y = len(grid[0])
        q = deque()
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        
        q.append([sx, sy])
        mark[(sx, sy)]

        while q:
            cx, cy = q.pop()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < x and 0 <= ny < y and grid[nx][ny] == "1" and mark[(nx, ny)] == False:
                    mark[(nx, ny)] = True
                    q.appendleft([nx, ny])


    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mark[(i, j)] = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if mark[(i, j)] == False and grid[i][j] == "1":
                    res += 1
                    self.bfs(grid, i, j)

        return res

