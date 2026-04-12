class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        sliding window baby
        '''
        l = 0
        r = len(s1)-1
        if len(s2) < len(s1): return False
        if len(s1) == 0: return True
        print(s1)
        vals = defaultdict(int)
        for i in s1:
            vals[i] +=1
        while r < len(s2):
            print(s2[l:r+1])
            opp = defaultdict(int)
            for j in s2[l:r+1]:
                opp[j] +=1
            if vals == opp: return True

            l+=1
            r+=1
        return False