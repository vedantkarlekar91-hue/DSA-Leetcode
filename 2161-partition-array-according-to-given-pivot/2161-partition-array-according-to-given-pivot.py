class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if nums[i]<pivot:
                arr1.append(nums[i])

        
        for i in range(len(nums)):
            if nums[i]==pivot:
                arr1.append(nums[i])

        for i in range(len(nums)):
            if nums[i]>pivot:
                arr2.append(nums[i])
        
        arr = arr1 + arr2
        return arr
        