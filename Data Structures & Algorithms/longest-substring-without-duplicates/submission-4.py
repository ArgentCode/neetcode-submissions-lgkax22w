class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        max_len = 0
        if len(s) == 1: return 1
        if len(s) == 0: return 0
        while r < len(s):
            val = s[r]
            for i in range(l, r):
                if val == s[i]:
                    l = i+1
            r+=1
            max_len = max(max_len, r-l)
        return max_len