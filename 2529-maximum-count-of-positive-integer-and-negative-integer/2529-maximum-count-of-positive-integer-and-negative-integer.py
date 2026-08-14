class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pass
            elif nums[i] < 0:
                neg+=1
            else:
                pos += 1
        if pos > neg:
            return pos
        else:
            return neg