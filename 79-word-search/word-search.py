class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        if len(word) > m * n: return False

        boardDict = defaultdict(int)
        for i in range(m):
            for j in range(n):
                boardDict[board[i][j]] += 1
        
        wordDict = Counter(word)
        for c in wordDict:
            if c not in boardDict or wordDict[c] > boardDict[c]:
                return False

        def backtrack(idx: int, r: int, c: int) -> bool:
            if idx == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False

            tmp = False
            board[r][c] = "-"
            tmp = backtrack(idx + 1, r + 1, c) or \
                backtrack(idx + 1, r - 1, c) or \
                backtrack(idx + 1, r, c + 1) or \
                backtrack(idx + 1, r, c - 1)
            board[r][c] = word[idx]
            return tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j): return True

        return False