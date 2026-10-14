class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        arr = []
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        sorted_freq = dict(sorted(freq.items(), key = lambda item:item[1], reverse = True))

        for i in range(k):
            key = list(sorted_freq.keys())[i]
            arr.append(key)
        return arr