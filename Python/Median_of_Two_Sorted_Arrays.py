# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        len_merged_array = len(merged_array)
        middle_number = len_merged_array//2
        if len_merged_array % 2 == 0:
            return (merged_array[middle_number] + merged_array[middle_number-1])/2
        return merged_array[middle_number]
