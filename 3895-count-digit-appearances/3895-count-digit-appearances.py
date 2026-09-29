class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            while n>0:
                n1 = n % 10
                n = n // 10

                if n1 == digit:
                    count+=1
        return count 