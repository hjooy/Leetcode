class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(i) -> int:
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j: 
                if rank[root_i] >= rank[root_j]:
                    parent[root_j] = root_i
                    rank[root_i] += rank[root_j]
                else:
                    parent[root_i] = root_j
                    rank[root_j] += rank[root_i]
        
        if not nums:
            return 0

        parent, rank = {}, {}

        for n in nums:
            parent[n] = n
            rank[n] = 1
        
        for n in nums:
            if n - 1 in rank:
                union(n, n - 1)
            if n + 1 in rank:
                union(n, n + 1)
        
        return max(rank.values())