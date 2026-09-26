class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_length = min(len(first), len(last))
        for i in range(min_length):
            if first[i] != last[i]:
                return first[:i]
        
        return first[:min_length]


        