class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        hz = False
        for i in range(n):
            s += nums[i]
            if nums[i] == 0:
                hz = True
        
        if not hz:
            return 0

        return (n * (n + 1) // 2 - s)