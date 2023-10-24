class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))

        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
            
        return ans