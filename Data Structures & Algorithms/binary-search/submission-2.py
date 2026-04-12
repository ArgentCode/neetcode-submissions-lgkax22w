class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = int(r/2)
        iter = 0
        while l < r or l != r:
            print("Considering", nums[l:r])
            print(l,mid,r)
            if target == nums[mid]:
                print("Found it!")
                return mid
            elif target > nums[mid]:
                print(target, "> ", nums[mid])
                l = mid
            elif target < nums[mid]:
                print(target, "< ", nums[mid])
                r = mid
            
            if l+1 ==r:
                if target == nums[l]:
                    return l
                else: 
                    return -1
            mid = int((l+r)/2)
            iter += 1
            #if iter > 5: return 10
        return -1


        