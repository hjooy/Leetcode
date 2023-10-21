class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_map.keys())[:k]
        
# Time complexity: O(n log n)
# Space complexity: O(n)