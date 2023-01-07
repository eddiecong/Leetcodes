# 890. Find and Replace Pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            d = {}
            s = {}
            is_valid = True
            if len(word) != len(pattern):
                continue

            for i in range(len(word)):
                if pattern[i] not in d:
                    d[pattern[i]] = word[i]
                else:
                    if d[pattern[i]] != word[i]:
                        is_valid = False
                        break
                        
                if word[i] not in s:
                    s[word[i]] = pattern[i]
                else:
                    if s[word[i]] != pattern[i]:
                        is_valid = False
                        break
            if is_valid:
                output.append(word)
        return output
