class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = defaultdict(int)
        for n in nums:
            vals[n] +=1
        results = []
        while k > 0:
            big = 0
            big_key = None
            for key, value in vals.items():
                if value > big:
                    big_key = key
                    big = value
            results.append(big_key)
            vals.pop(big_key)
            k -=1
        return(results)
        