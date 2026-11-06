class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        groups = {}
        
        for i in range(n):
            if nums[i] not in groups:
                groups[nums[i]] = []

            groups[nums[i]].append(i)

        for indices in groups.values():
            m = len(indices)

            if m == 1:
                continue

            total = sum(indices)
            left = 0

            for k in range(m):
                i = indices[k]

                right = total - left - i

                arr[i] = (i * k - left) + (right - i * (m - k - 1))

                left += i

        return arr