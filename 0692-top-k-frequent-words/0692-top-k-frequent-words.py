class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        arr = []
        for i in range(len(words)):
            if words[i] in freq:
                freq[words[i]] += 1
            else:
                freq[words[i]] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

        for i in range(k):
            arr.append(sorted_freq[i][0])
        return arr