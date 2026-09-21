class Solution:
    def findWordsContaining(self, words, x):
        ans = []

        for i in range(len(words)):
            word = words[i]

            for ch in word:
                if ch == x:
                    ans.append(i)
                    break

        return ans