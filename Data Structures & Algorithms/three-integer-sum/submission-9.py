class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # because otherwise its all positive
            if a > 0:
                break

            # duplicate i indexes essentially
            if i > 0 and a == nums[i - 1]:
                continue
            # set pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # if too big, get the next smallest big number
                if threeSum > 0:
                    r -= 1
                # if too small, get the nexxt biggest small number
                elif threeSum < 0:
                    l += 1
                #if goldilocks, add!
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip any duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res