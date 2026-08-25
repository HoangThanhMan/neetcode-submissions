class Solution:
    '''
        Summary idea: 
            We use hash sets to keep track of the values seen in each row and column
        from 1 to 9. For the 3x3 sub-boxes, we apply a technique that maps each cell
        to a corresponding sub-box using the (row // 3, col // 3) tuple as the key.
        If a value is already present in any of the corresponding row, column, or 
        sub-box set, the board is invalid. Otherwise, we add the value to each set.
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):

                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
        
