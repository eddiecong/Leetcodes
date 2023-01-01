class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Generate the codes inside the word patterns.
        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))
