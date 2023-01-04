# Key Idea:
# 1. Divide the round number into two cases, mod 3 is 0 or mod 3 is not 0.

# Reference Link:
# Question name: 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """Seperate the cases into three ways:
        1. 3k
        2. 3k + 1
        3. 3k + 2 
        """
        integer_dict = {}
        for task in tasks:
            if task in integer_dict.keys():
                integer_dict[task] += 1
            else:
                integer_dict[task] = 1
        
        count = 0
        for key in integer_dict.keys():
            if integer_dict[key] == 1:
                return -1
            else:
                round_num = self.get_minimum_round_from_number(integer_dict[key])
                count += round_num
        return count
    
    def get_minimum_round_from_number(self, number: int) -> int:
        division = number % 3
        if division == 0: return int(number / 3)
        else: return int(number / 3 + 1)
