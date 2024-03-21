class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:
            for i in range(c, target + 1):
                if i == c: 
                    dp[i].append([c])
                    continue
                for com in dp[i - c]:
                    dp[i].append(com + [c])
        return dp[-1];

    # Does list concatenation with the `+` operator always return a new `list` instance?
    # https://stackoverflow.com/questions/64644671/does-list-concatenation-with-the-operator-always-return-a-new-list-instanc
    # The reference documentation does not explicitly guarantee that :list + :list results in a new list. However, it is implied by the += augmented assignment being explicitly in-place if possible in contrast to the + operator.