class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # count = 0
        # candidate = 0

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1

        # return candidate

        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        result = max(freq, key=freq.get)
        return result
