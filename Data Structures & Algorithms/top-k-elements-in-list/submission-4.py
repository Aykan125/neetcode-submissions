class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        mapping= {}
        output = []
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i] = 1
        for j in mapping.keys():
            heapq.heappush(maxHeap, (-1*mapping[j], j))
        
        for r in range(k):
            output.append(heapq.heappop(maxHeap)[1])
        return output
        
        