class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            res = [0]*26
            for j in i:
                res[ord(j) - ord("a")] +=1
            groups[tuple(res)].append(i)
        return [i for i in groups.values()]

