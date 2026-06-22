import heapq
class Solution:
    def kthSmallest(self, arr, k):
        pq = []
        
        for i in range(len(arr)):
            heapq.heappush(pq, -arr[i]) 
            
            if len(pq) > k:
                heapq.heappop(pq)
                
        return -pq[0]
