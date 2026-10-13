class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        result = nums1 + nums2
        result.sort()
        if len(result) % 2 != 0:
            mid = (len(result))//2
            return result[mid]
        else:
            mid = (len(result)//2)
            New_result = (result[mid-1] + result[mid])/2
            return New_result