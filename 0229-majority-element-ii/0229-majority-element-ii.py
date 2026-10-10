class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hash_map = {}
        count = len(nums)//3

        arr = []

        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        for key, value in hash_map.items():
            if value > count:
                arr.append(key)
        return arr