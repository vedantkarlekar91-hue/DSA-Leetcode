class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for i in range(len(sentences)):
            words = sentences[i].split()
            arr.append(len(words))
        return max(arr) 