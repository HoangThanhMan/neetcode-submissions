class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rlo = 0
        rhi = len(matrix) - 1
        ok = False
        while rlo <= rhi:
            mid = int((rlo + rhi)/2)
            if matrix[mid][0] == target:
                ok = True
                break
            
            if matrix[mid][0] < target:
                rlo = mid + 1
            elif matrix[mid][0] > target:
                rhi = mid - 1
        
        row = rhi

        clo = 0
        chi = len(matrix[0]) - 1
        while clo <= chi:
            mid = int((clo + chi)/2)
            if matrix[row][mid] == target:
                ok = True
                break
            
            if matrix[row][mid] < target:
                clo = mid + 1
            elif matrix[row][mid] > target:
                chi = mid - 1

        return ok

