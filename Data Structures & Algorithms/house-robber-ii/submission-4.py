# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]

#         if len(nums) == 2:
#             return max(nums[0], nums[1])

#         dp1 = [0] * len(nums)
#         dp2 = [0] * len(nums)

#         dp1[0] = nums[0]
#         dp1[1] = max(nums[0], nums[1])

#         dp2[1] = nums[1]
#         dp2[2] = max(nums[1], nums[2])

#         for i in range(2, len(nums) - 1):
#             dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
#         for i in range(3, len(nums)):
#             dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])

#         return max(dp1[-1] , dp2[-1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Thêm base case để tránh lỗi Index Out of Bounds cho mảng có 2 phần tử
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n

        # dp1: Xét từ nhà 0 đến nhà n-2 (bỏ qua nhà cuối)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        # dp2: Xét từ nhà 1 đến nhà n-1 (bỏ qua nhà đầu)
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])

        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
            
        for i in range(3, n):
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])

        # Trả về dp1 tại vị trí n-2 (vì dp1 bỏ qua nhà cuối cùng) và dp2 tại n-1
        return max(dp1[n - 2], dp2[n - 1])