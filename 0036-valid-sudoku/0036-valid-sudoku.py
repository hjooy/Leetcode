class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = []

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != ".":
                    ans += [(i, number), (number, j), (i//3, j//3, number)]
        
        return len(ans) == len(set(ans))