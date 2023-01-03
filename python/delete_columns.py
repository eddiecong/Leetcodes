class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_count = 0
        str_length = len(strs[0])
        for i in range(str_length):
            last = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] < last:
                    del_count += 1
                    break
                last = strs[j][i]
        return del_count
