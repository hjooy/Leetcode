class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = set(numbers)
        for i, n1 in enumerate(numbers, 1):
            if target - n1 in num_set:
                for j, n2 in enumerate(numbers[i:], i + 1):
                    if n2 == target - n1:
                        return [i, j]

        return []