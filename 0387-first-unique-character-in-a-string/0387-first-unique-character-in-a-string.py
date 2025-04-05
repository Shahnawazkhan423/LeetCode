class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count= {}
        for ch in s:
            if ch in char_count:
                char_count[ch]+=1
            else:
                char_count[ch]=1

        for k in range(len(s)):
            if char_count[s[k]]==1:
                return k

        return -1