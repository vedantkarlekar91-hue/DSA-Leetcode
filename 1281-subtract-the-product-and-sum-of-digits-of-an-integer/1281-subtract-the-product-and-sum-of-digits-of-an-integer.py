class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digit = 1
        sum = 0
        while n > 0:
            num = n % 10
            n = n // 10
            product_of_digit *= num
            sum += num

        return product_of_digit - sum