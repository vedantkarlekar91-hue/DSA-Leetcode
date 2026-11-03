class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(len(nums)-1):
            total += nums[len(nums)-1] - nums[i]
        return total