class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for j in t:
            t_dict[j] += 1
        
        for key, value in s_dict.items():
            if value != t_dict.get(key): return False
        return True
