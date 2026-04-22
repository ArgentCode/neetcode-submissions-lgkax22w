from collections import defaultdict
def string_to_dict(s: str):
    res = defaultdict(int)
    for i in s:
        res[i] +=1 
    return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        print(res)
        return list(res.values())