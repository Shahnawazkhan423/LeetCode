class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        common_prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i]==last[i]:
                common_prefix+=first[i]
            else:
                break 
        return common_prefix