from string import punctuation

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for punctuation in ',=+:_.?;"-\' ':
            s = s.replace(punctuation, "")
        n = len(s)
        i =0
        j = n-1
        print(s)
        while i < j:
            if s[i] != s[j]: 
                print("failed on:", s[i], s[j])
                return(False)
            i = i+1
            j = j -1
        return(True)