class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        r = len(nums)
        
        single_digit_sum = 0
        double_digit_sum = 0
        
        for i in range(0,r):
            if nums[i] < 10:
                single_digit_sum += nums[i]
            else:
                double_digit_sum += nums[i]

        if single_digit_sum != double_digit_sum:
            return True
        else:
            return False