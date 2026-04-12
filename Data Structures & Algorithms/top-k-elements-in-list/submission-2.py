class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        for i in nums:
            values[i] = 1 + values.get(i, 0)
        results = []
        for i in range(k):
            biggest_key = None
            biggest_val = -1
            for key, count in values.items():
                if count > biggest_val:
                    biggest_val = count
                    biggest_key = key
            results.append(biggest_key)
            values.pop(biggest_key)
        return(results)
        