class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            num = i
            cnt = 0
            while num > 0:
                cnt += num & 1
                num >>= 1
            res.append(cnt)

        return res        