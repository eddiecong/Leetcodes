# 792. Number of Matching Subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Use a dictionary to hold the characters appeared in the sequence, store the list of index appeared.
        def have_larger_index(list1, list2):
            for i in list2:
                for j in list1:
                    if i > j:
                        return True
            return False
        
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = [i]
            else:
                dict[s[i]].append(i)
        
        count = 0
        for i in range(len(words)):
            word = words[i]
            is_tar = True
            last_list = [0]
            for j in range(len(word)):
                if word[j] not in dict:
                    is_tar = False
                    break
                else:
                    cur_list = dict[word[j]]
                    if not have_larger_index(last_list, cur_list):
                        is_tar = False
                        break
                    else:
                        last_list = cur_list

            if is_tar:
                count += 1
                
        return count
