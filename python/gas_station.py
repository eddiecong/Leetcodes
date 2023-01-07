# Key Idea:
# 1. If sum of gas is less than sum of cost, then return -1.
# 2. Only one solution.
# 3. If starting with index a, and index b is done, then the answer is from b.

# Reference Link:
# Question name: 134. Gas Station
# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """solution function inside the codebase.
        """
        if sum(gas) < sum(cost): return -1
        count = idx = 0
        for i in range(len(gas)):
            count += gas[i] - cost[i]
            if count < 0: count, idx = 0, i+1
        return idx
