class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = {}
        result1 = ""
        mid = ""

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sorted_freq = dict(sorted(freq.items()))

        for key, value in sorted_freq.items():
            result1 += key * (value // 2)

            # Find the middle character, if any
            if value % 2 != 0:
                mid = key

        # Reverse the first half
        result2 = result1[::-1]

        # Construct the smallest palindrome
        return result1 + mid + result2

