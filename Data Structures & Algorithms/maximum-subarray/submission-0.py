class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSub = 0, nums[0]
        
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSub = max(maxSub, curSum)

        return maxSub