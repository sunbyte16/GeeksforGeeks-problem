import heapq

class Solution:
    def kthSmallest(self, arr, k):
        heapq.heapify(arr)  # convert to min heap
        
        for _ in range(k - 1):
            heapq.heappop(arr)
        
        return heapq.heappop(arr)
