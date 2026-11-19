class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m=0
        a=[]
        s=set(nums)
       
        for i in s:
            v=nums.count(i)
            a.append(v)
            if v>m:
                m=v
        return a.count(m)*m
        