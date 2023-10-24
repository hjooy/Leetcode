class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = sum(
            ([(row_num, n), (n, col_num), (row_num//3, col_num//3, n)]
            for row_num, row in enumerate(board)
                for col_num, n in enumerate(row)
                    if n != "."), []) 
            # sum() usage: flattening a list of lists

        return len(seen) == len(set(seen))