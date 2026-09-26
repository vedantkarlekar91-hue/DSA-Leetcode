class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        Max = max(candies)
        arr= []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= Max:
                arr.append(True) 
            else:
                arr.append(False)
        return arr