class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]]+=1
        freq = [[] for _ in range(len(nums)+1)]
        for key in count.keys():
            freq[count[key]].append(key)
        res = []
        for j in range(len(freq)-1, -1, -1):
            # print(j)
            for r in freq[j]:
                res.append(r)
                if len(res) == k:
                    return res



        