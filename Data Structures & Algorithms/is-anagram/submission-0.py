class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return(False)
        n = len(s)
        vals = {}
        for i in range(n):
            if vals.get(s[i]) == None:
                vals[s[i]] = 1
            else:
                vals[s[i]] = vals[s[i]]+1
        
        for i in range(n):
            if vals.get(t[i]) == None:
                return False
            else:
                vals[t[i]] = vals[t[i]]-1

        for value in vals.values():
            if value > 0:
                return False
        
        return(True)