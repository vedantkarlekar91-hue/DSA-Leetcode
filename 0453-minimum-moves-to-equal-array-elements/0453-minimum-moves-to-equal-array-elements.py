class Solution:
    def minMoves(self, nums: list[int]) -> int:

        # nums.sort()
        # total = 0

        # while nums[0] != nums[len(nums)-1]:
        #     last_element = nums[len(nums)-1]
        #     first_element = nums[0]
        #     diff = last_element - first_element
        #     total += diff

        #     for i in range(len(nums) - 1):
        #         nums[i] += diff
        #     nums.sort()
        
        # return total
        nums.sort()
        total = 0
        for i in range(len(nums)-1,0,-1):
            diff = nums[i] - nums[0]
            total += diff 
        return total









