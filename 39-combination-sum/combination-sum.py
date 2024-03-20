class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def helper(idx: int, sum: int, com: List[int]):
            if sum > target: return
            elif sum == target:
                result.append(com);
                return;
            for i in range(idx, n):
                helper(i, sum + candidates[i], com + [candidates[i]])
            
        helper(0, 0, []);
        return result;

    # Does list concatenation with the `+` operator always return a new `list` instance?
    # https://stackoverflow.com/questions/64644671/does-list-concatenation-with-the-operator-always-return-a-new-list-instanc
    # The reference documentation does not explicitly guarantee that :list + :list results in a new list. However, it is implied by the += augmented assignment being explicitly in-place if possible in contrast to the + operator.