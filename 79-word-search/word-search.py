class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        result = [False]
        m = len(board)
        n = len(board[0])
        visited = set()

        def backtrack(idx: int, r: int, c: int, visited: Set[Tuple[int]]):
            if idx == len(word):
                result[0] = True
                return

            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or board[r][c] != word[idx]:
                return

            visited.add((r, c))
            for direction in directions:
                backtrack(idx + 1, r + direction[0], c + direction[1], visited)
            visited.remove((r, c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    backtrack(0, i, j, visited)
                if result[0]: break

        return result[0]