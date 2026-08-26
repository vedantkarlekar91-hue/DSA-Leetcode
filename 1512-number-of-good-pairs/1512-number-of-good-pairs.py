class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[i] == nums[j]:
                    count += 1
        return count