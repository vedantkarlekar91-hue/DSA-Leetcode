class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        
        left = 0
        right = len(nums)-1
        while left < right:
            total = nums[left] + nums[right]

            if total == target:
                return left + 1, right + 1
                break
            elif total > target:
                right -= 1
            else:
                left += 1
        