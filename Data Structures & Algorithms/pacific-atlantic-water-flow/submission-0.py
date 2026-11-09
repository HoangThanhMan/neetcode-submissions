class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        res = []
        def dfs(r, c, visit, pv):
            if (r, c) in visit or c < 0 or r < 0 or c >= col or r >= row or heights[r][c] < pv:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1][c])
        
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
            
        return res

