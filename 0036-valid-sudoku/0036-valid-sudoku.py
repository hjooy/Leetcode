class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = sum(
            ([(row_num, n), (n, col_num), (row_num//3, col_num//3, n)]
            for row_num in range(9) for col_num in range(9)
            for n in board[row_num][col_num]
            if n != "."), []) 
            # sum() usage: flattening a list of lists

        return len(seen) == len(set(seen))