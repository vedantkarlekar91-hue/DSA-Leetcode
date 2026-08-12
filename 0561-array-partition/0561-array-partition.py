class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        arr = []
        for i in range(0,len(nums),2):
            arr.append(nums[i])
        return sum(arr)

        