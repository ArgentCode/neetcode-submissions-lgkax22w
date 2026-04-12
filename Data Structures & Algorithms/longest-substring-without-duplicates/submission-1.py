class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2: return(n)
        maxWord = 1
        word = ''
        for i in range(n):
            if len(word) > maxWord: 
                maxWord = len(word)
            word = s[i]
            for j in range(i+1,n):
                print(word, "and", s[j])
                if s[j] not in word:
                    word = word + s[j]
                else:
                    if len(word) > maxWord: 
                        maxWord = len(word)
                    break
        
        if len(word) > maxWord: 
            maxWord = len(word)
        return(maxWord)

        