class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid(row): return False

        for col in zip(*board):
            if not self.is_valid(col): return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid(sub_box): return False
        
        return True

    def is_valid(self, input) -> bool:
        seen = [n for n in input if n != "."]
        return len(seen) == len(set(seen))