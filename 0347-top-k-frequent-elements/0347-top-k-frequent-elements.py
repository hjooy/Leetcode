class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(nums), 0, -1):
            if bucket[i] is None : continue
            for num in bucket[i]:
                if k == 0: break
                ans.append(num)
                k -= 1
        
        return ans