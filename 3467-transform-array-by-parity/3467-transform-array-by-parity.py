class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)):
            if nums[n] % 2 == 0:
                nums[n] = 0
            else:
                nums[n] = 1
        
        nums.sort()
        return nums