# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_array = []
        current_total = 0

        for num in nums:
            current_total += num
            new_array.append(current_total)

        return new_array
