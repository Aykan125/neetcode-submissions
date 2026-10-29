class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        mapping= {}
        output = []
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i] = 1
        for j in mapping.keys():
            if len(minHeap)<k:
                heapq.heappush(minHeap, (mapping[j], j))
            else:
                if mapping[j] > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (mapping[j], j))
        minHeap.reverse()
        for i, j in minHeap:
            output.append(j)
        return output
        
        