class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        return nums[l-k]