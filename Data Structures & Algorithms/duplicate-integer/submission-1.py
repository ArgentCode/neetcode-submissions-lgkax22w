class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if dict.get(i) != None: return True
            dict[i] = 0
        return False