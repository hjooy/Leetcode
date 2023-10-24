class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        return not any(x in seen or
                        seen.add(x)
                        for row_num, row in enumerate(board)
                        for col_num, n in enumerate(row)
                        if n != "."
                        for x in ((n, row_num), (col_num, n), (row_num//3, col_num//3, n)))
                        # set.add() always returns None