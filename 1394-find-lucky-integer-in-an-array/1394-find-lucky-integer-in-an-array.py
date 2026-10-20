class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = {}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
    
        sorted_freq = dict(sorted(freq.items(), reverse = True))
        for key, value in sorted_freq.items():
            if key == value:
                return key
            
        return -1