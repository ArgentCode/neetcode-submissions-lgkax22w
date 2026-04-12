class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        for i in nums:
            if results.get(i) == None:
                results[i] = 1
            else:
                results[i] = results[i] +1
        final_results = []
        for i in range(k):
            biggest_key = None
            biggest_count = 0
            for key, count in results.items():
                if count > biggest_count:
                    biggest_key = key
                    biggest_count = count
            results.pop(biggest_key)
            final_results.append(biggest_key)
        return(final_results)