import heapq
from collections import Counter
class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        pq = []
        for num, freq in counts.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k: heapq.heappop(pq)
        return [pair[1] for pair in pq]
    
class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return [num for num, count in Counter(nums).most_common(k)]