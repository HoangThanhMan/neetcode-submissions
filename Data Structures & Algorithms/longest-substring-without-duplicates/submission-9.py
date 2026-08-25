class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        ans = 0

        for r, c in enumerate(s):
            if c in seen:
                l = max(seen[c] + 1, l)
            seen[c] = r
            ans = max(ans, r - l + 1)

        return ans