class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        print(newStr)
        # if len(newStr) < 2:
        #     return False

        l,r = 0, len(newStr)-1

        while r > l:
            if newStr[l] != newStr[r]:
                return False

            l += 1
            r -= 1

        return True