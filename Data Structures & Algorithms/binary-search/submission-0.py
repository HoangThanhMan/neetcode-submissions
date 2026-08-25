class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        ans = -1
        while lo <= hi:
            mid = int((lo + hi)/2)
            if nums[mid] == target:
                ans = mid
                break
            
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        
        return ans