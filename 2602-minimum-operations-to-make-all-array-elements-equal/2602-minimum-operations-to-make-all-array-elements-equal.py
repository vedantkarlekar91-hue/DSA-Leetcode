class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()

        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        answer = []
        n = len(nums)

        for q in queries:

            left = 0
            right = n

            # Binary Search
            while left < right:
                mid = (left + right) // 2

                if nums[mid] < q:
                    left = mid + 1
                else:
                    right = mid

            idx = left

            left_operations = (q * idx) - prefix[idx]

            right_operations = (prefix[n] - prefix[idx]) - (q * (n - idx))

            answer.append(left_operations + right_operations)

        return answer