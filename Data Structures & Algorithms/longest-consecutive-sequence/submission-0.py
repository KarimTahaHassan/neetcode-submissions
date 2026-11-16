class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1

        hashmap_2 = {}
        res = 0
        for n in nums:
            max_n = 1
            if n-1 not in hashmap:
                j = n + 1
                while j in hashmap:
                    max_n += 1
                    j += 1

                if max_n > res:
                    res = max_n

        return res
                
