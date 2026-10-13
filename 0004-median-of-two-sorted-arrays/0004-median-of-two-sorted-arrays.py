class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        merge_array = nums1 + nums2
        merge_array.sort()
        if len(merge_array) % 2 != 0:
            mid = (len(merge_array))//2
            return merge_array[mid]
        else:
            mid = (len(merge_array)//2)
            New_result = (merge_array[mid-1] + merge_array[mid])/2
            return New_result