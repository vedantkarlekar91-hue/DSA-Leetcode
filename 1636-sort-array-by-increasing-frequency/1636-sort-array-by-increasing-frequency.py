class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        arr = []
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        sorted_freq = dict(sorted(freq.items(), key = lambda x:(x[1], -x[0])))

        for key, value in sorted_freq.items():
            for i in range(value):
                arr.append(key)
        
        return arr