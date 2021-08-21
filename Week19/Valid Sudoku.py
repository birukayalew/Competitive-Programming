class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_column = defaultdict(lambda : set())
        square = defaultdict(lambda : set())
        
        for i in range(9):
            for j in range(9):
                curr = (i // 3) * 3 + (j // 3)
                
                if board[i][j] != '.' and (board[i][j] in row_column[i] or board[i][j] in row_column[~j] or board[i][j] in square[curr]):
                    
                    return False
                
                row_column[i].add(board[i][j])
                row_column[~j].add(board[i][j])
                square[curr].add(board[i][j])
        
        return True
