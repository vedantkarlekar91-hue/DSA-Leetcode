class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            sum = 0
            n1 = nums[i]
            while n1 > 0:
                num = n1 % 10
                n1 = n1 // 10
                sum += num
            
            if sum == i:
                return i 
                break
        return -1