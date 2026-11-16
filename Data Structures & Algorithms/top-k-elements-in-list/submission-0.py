class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        counts = {}
        for i in range(len(nums)+1):
            counts[i] = []

        for n, c in hashmap.items():
            counts[c].append(n)

        res = []
        for i in range(len(counts)-1, -1, -1):
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res
