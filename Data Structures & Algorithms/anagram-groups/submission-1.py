class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        n = len(s)
        if len(s) != len(t): return False
        vals = {}
        for i in range(n):
            if vals.get(s[i]) == None:
                vals[s[i]] = 1
            else:
                vals[s[i]] = vals[s[i]] + 1
        
        for i in range(n):
            if vals.get(t[i]) == None:
                return(False)
            else: 
                vals[t[i]] = vals[t[i]] -1
        
        for value in vals.values():
            if value != 0: return(False)
        return(True)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        while len(strs) > 0:
            temp_list = []
            val = strs.pop()
            temp_list.append(val)
            for s in strs:
                if self.isAnagram(val, s):
                    temp_list.append(s)
            
            for i in range(1, len(temp_list)):
                item = temp_list[i]
                strs.remove(item)
            
            results.append(temp_list)
        return(results)


        