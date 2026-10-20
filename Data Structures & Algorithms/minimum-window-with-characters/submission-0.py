class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        mp1, mp2 = {}, {}

        for c in t:
            mp1[c] = 1 + mp1.get(c, 0)

        res, rLen = [-1, -1], float("infinity")
        
        cnt1, cnt2 = 0, len(mp1)
        l = 0
        for r in range(len(s)):
            c = s[r]
            mp2[c] = 1 + mp2.get(c, 0)
            if c in mp1 and mp1[c] == mp2[c]:
                cnt1 += 1
            while cnt1 == cnt2:
                if r - l + 1 < rLen:
                    res = [l, r]
                    rLen = r - l + 1    
                mp2[s[l]] -= 1
                if s[l] in mp1 and mp2[s[l]] < mp1[s[l]]:
                    cnt1 -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if rLen != float("infinity") else ""
        