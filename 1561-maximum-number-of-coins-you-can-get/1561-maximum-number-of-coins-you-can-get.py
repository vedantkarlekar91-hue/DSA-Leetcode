class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        arr = []
        nums = []
        piles.sort()
        a = len(piles)-1
        n = len(piles)//3
     
        for i in range(0,n):
            arr.append(piles[i])
            arr.append(piles[a-(2*i)])
            arr.append(piles[a-((2*i)+1)])
            arr.sort()
            nums.append(arr[1])
            arr.clear()
        return sum(nums)