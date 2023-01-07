# Key Ideas:
# 1. left should be mid + 1 and right should be right - 1 when updating.
# 2. Edge cases.

# Reference Link:
# Question name: 704. Binary Search
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p, q = 0, len(nums) - 1
        while p <= q:
            mid = (p + q) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1
        return -1