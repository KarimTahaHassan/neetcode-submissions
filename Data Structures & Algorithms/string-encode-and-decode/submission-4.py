class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string = string+ str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) < 1:
            return []
        
        res, end = [], 0
        while end < len(s):
            start = end
            while s[end] != "#":
                end +=1
            length = int(s[start:end])

            start = end+1
            end += length+1
            string = ""
            for i in range(start, end):
                string += s[i]
            res.append(string)
        return res
