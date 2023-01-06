class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        return self.count_stairs(n, d)
        
    def count_stairs(self, n, d):
        if n == 0 or n == 1: return 1
        if n in d: return d[n]
        
        output = self.count_stairs(n-1, d) + self.count_stairs(n-2, d)
        d[n] = output
        return output
