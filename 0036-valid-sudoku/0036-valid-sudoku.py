class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        return 1 == max(list(Counter(x
                        for row_num, row in enumerate(board)
                        for col_num, n in enumerate(row)
                        if n != "."
                        for x in ((n, row_num), (col_num, n), (row_num//3, col_num//3, n))).values()) + [1])
                        # .append(1) instead of + [1] does not work. append() returns None in Python