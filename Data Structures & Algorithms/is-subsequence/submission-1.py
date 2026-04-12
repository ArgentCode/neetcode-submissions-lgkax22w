class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s is a subsequence of t while preserving order
        # Basically, I need two points. One on s and one on t. 
        # lo
        if s == "": return True
        if len(t) < len(s): return False
        n = len(t)
        j = 0
        char = s[j]
        for c in t:
            if c==char:
                j += 1
                if j == len(s): return True
                char = s[j]
        
        return False

                    


        