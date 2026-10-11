class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item:item[1]))

        rev = ""
        for key, value in reversed(sorted_freq.items()):
            rev +=(key * value)
        
        return rev