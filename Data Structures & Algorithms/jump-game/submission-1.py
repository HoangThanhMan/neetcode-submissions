class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)  

        n = len(nums)
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                dp[i] = max(dp[min(n - 1, i + j)], dp[i])

        return dp[0]