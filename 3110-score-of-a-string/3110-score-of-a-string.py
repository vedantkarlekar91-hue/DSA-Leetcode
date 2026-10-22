class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = []
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])
            result = a - b
            arr.append(abs(result))
        total = sum(arr)
        return total