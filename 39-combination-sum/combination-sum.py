class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(i: int, sum: int, com: List[int]):
            if sum > target: return
            elif sum == target:
                result.append(com);
                return;
            sum += candidates[i]
            com1 = com[:]
            com1.append(candidates[i])
            helper(i, sum, com1)
            if i < len(candidates) - 1:
                sum -= candidates[i]
                com2 = com1[:-1]
                helper(i + 1, sum, com2)

        helper(0, 0, []);
        return result;