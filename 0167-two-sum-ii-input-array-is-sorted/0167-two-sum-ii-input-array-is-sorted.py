class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        for i, n1 in enumerate(numbers, 1):
            if target - n1 in num_set:
                for j in range(i, len(numbers)):
                    if numbers[j] + n1 == target:
                        return [i, j + 1]

        return []