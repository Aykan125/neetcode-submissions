class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[x**2+y**2, x, y] for x,y in points]
        heapq.heapify(heap)
        output = []
        while k>0:
            _, x, y = heapq.heappop(heap)
            output.append([x,y])
            k-=1
        return output

        