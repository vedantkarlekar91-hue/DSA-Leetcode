class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            order = ord(s[i])
            sequence_order = abs(order - 123)
            result = sequence_order * (i+1)
            total += result
        return total