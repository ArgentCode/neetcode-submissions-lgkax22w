class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        n = len(nums)
        for i in range(n):
            val1 = nums[i]
            # i is the number not to include
            total = 1
            for j in range(n):
                val2 = nums[j]
                if i == j: continue
                total = total * val2
            results.append(total)
        return results