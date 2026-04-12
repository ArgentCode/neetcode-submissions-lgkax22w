class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        vals = {}
        for i in range(n):
            print(vals.get(nums[i]))
            if vals.get(nums[i]) == None:
                vals[nums[i]] = True
            else:
                return(True)
        return(False)
        