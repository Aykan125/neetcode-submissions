class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-i for i in stones]
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            stone1 = (-1)*heapq.heappop(minHeap)
            stone2 = (-1)*heapq.heappop(minHeap)
            if stone1 == stone2:
                continue
            heapq.heappush(minHeap, (-1)*(stone1-stone2))
        if minHeap:
            return -1*minHeap[0]
        else:
            return 0
            
        