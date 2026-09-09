class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        rev = ""
        for i in range(len(words)):
            for ch in words[i]:
                rev = ch + rev

            if words[i] == rev:
                break
            else:
                rev = ""
        return rev
                