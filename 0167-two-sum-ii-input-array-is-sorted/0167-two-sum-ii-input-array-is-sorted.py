class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(numbers, 1):
            if target - n in dict:
                return [dict[target - n], i]
            dict[n] = i

        return []