class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        averages = []
        l = len(nums) - 1
        for i in range(len(nums)):
            if i == len(nums)//2:
                break
            else:
                averages.append((nums[i] + nums[l-i])/2)
        averages.sort()
        return averages[0]