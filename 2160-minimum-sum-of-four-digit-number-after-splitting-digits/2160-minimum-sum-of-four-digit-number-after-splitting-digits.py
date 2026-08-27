class Solution(object):
    def minimumSum(self, num):
        nums = []
        string = str(num)
        for i in range(len(string)):
            nums.append(string[i])
        nums.sort()
        num1 = nums[0] + nums[3]
        num2 = nums[1] + nums[2]
        new1 = int(num1)
        new2 = int(num2)
        return new1 + new2