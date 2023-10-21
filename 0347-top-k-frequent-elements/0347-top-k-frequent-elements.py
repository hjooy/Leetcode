class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        ans = []
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        
        for key in sorted_map.keys():
            if len(ans) >= k:
                break
            ans.append(key)
        return ans
        
# Time complexity: O(n log n)
# Space complexity: O(n)