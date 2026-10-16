class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
    
        for i in range(len(nums)):
            rev = 0
            temp = nums[i]
            while temp >0:
                n = temp % 10
                temp = temp // 10
                rev = rev * 10 + n
            nums.append(rev)
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        return len(freq)
                