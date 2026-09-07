class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            n1 = n % 10
            n = n // 10

            if num % n1 == 0:
                count += 1
        
        return count