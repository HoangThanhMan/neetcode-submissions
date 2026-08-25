class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l 
        l, r = 0, len(nums) - 1
        if target <= nums[r] and target >= nums[pivot]:
            l = pivot
        else:
            r = pivot - 1

        res = -1
        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                res = m
                break

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return res


