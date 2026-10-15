class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = {}
        even_freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        for key in freq:
            if key % 2 == 0:
                even_freq[key] = freq[key]
            
        if not even_freq:
            return -1

        even_sorted_freq = dict(sorted(even_freq.items(), key = lambda item:item[0]))

        result = max(even_sorted_freq, key=even_sorted_freq.get)
        return result