class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))  + "@" + s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            slen = ""
            while s[i] != "@":
                slen += s[i]
                i += 1
            j = int(slen)
            res.append(s[i + 1: i + j + 1])
            i += j + 1
        return res