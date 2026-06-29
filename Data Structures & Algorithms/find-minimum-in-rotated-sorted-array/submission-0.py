class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[mid]







        







# 4, 5, 0, 1, 2, 3
# l = 0; r = 5
# mid = 2
# res = 0

