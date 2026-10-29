class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        nums.sort()
        
        if 1 not in nums:
                return 1
        if len(nums) < 2:
            if nums[0] < 0:
                pass
            else:
                return nums[0] + 1

        for i in range(len(nums)-1):    
            if nums[i] < 0:
                pass
            elif nums[i] == nums[i+1]:
                pass
            elif nums[i] + 1 != nums[i+1]:
                return nums[i] + 1
            else:
                pass
        
        return nums[len(nums)-1] + 1