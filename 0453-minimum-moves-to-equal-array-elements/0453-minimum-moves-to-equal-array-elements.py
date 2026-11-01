class Solution:
    def minMoves(self, nums: list[int]) -> int:

        nums.sort()
        total = 0

        for i in range(len(nums)-1,0,-1):
            diff = nums[i] - nums[0]
            total += diff 
        
        return total









