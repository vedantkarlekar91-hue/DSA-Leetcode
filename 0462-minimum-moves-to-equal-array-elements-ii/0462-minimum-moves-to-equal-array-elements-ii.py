class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        nums.sort()
        total = 0

        mid = len(nums)// 2        
        for i in range(len(nums)):
            total += abs(nums[i] - nums[mid])

        
        return total        