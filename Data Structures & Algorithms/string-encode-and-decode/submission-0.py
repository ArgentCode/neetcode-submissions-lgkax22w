class Solution:

    def encode(self, strs: List[str]) -> str:
        big_string = ''
        for s in strs:
            big_string = big_string + s + "{break}"
        print(big_string)
        return(big_string)

    def decode(self, s: str) -> List[str]:
        results = s.split("{break}")[:-1]
        print(results)
        return(results)