class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            first = nums[i]
            for j in range(i+1,n):
                second = nums[j]
                print(first, second)
                if first + second == target:
                    return([i, j])