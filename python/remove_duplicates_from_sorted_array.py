# Reference Link:
# Question name: 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Solve the question using dictionary:

        1. Create a dictionary which holds the result.
        2. Use an index to hold the correct indexing.
        """
        num_dict = {}
        non_duplicate_index = 0
        for i in range(len(nums)):
            if nums[i] not in num_dict.keys():
                num_dict[nums[i]] = 1
                nums[non_duplicate_index] = nums[i]
                non_duplicate_index += 1

        return non_duplicate_index
