'''
    1
    2 (0 2 3 2)
    2 (0 0 3 2)
    2 (0 0 1 2)
    1 (0 0 0 2)
    2 (0 0 0 0)

    (1/2 + 1) + (4/2) + (3/2 + 1) + (2/2) = 1 + 2 + 2 + 1 = 6
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

