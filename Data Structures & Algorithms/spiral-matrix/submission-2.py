class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a, b = 0, len(matrix)
        x, y = 0, len(matrix[0])

        res = []

        while x < y and a < b:
            for i in range(x, y):
                res.append(matrix[a][i])
            a += 1
            for i in range(a, b):
                res.append(matrix[i][y - 1])
            y -= 1
            if not (x < y and a < b): break
            for i in range(y - 1, x - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, a - 1, -1):
                res.append(matrix[i][x])    
            x += 1

        return res
