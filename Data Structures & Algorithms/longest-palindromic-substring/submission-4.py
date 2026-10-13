class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx, resLen = 0, 1
        n = len(s)

        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:

                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1

        return s[resIdx:resIdx + resLen]