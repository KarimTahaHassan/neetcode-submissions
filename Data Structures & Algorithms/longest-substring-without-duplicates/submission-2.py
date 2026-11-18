class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest_substring = 0
        l, r = 0, 0

        for i in range(len(s)):
            c = s[i]
            if c in hashmap:
                if hashmap[c] >= l:
                    longest_substring = max(longest_substring, r-max(l,1)+1)
                    l,r = hashmap[c]+1, i
                else:
                    r += 1
            else:
                r += 1
                    

            hashmap[c] = i
            

        return max(longest_substring, r-max(l,1)+1)

