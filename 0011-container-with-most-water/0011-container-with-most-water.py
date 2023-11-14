class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        i = 0
        j = len(height) - 1
        while i < j:
            amount = (j - i) * min(height[i], height[j])
            best = max(best, amount)
            if height[i] >= height[j]: j -= 1
            else: i += 1
        return best