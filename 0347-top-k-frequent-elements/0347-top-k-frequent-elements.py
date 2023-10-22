class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in count.items()]
        heapify(maxHeap)
        
        ans = []
        for _ in range(k):
            freq, num = heappop(maxHeap)
            ans.append(num)
        
        return ans