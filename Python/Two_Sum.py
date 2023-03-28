class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for index, value in enumerate(nums):
            value_needed = target - value

            if value_needed in seen_values:
                return [index, seen_values[value_needed]]
            seen_values[value] = index
