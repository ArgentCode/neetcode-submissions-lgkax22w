class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(filter(str.isalnum, s))
        clean_s = clean_s.lower()
        l = 0
        r = len(clean_s)-1
        print(clean_s)
        while l <= r:
            left = clean_s[l]
            right = clean_s[r]
            print("comparing", left, right)
            if clean_s[l] != clean_s[r]: return False
            l +=1
            r -=1
        return True