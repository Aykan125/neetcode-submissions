class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {i:set() for x in words for i in x}
        indegree = {i:0 for i in adj}

        for i in range(len(words) - 1):
            w1 , w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1)>len(w2):
                return ""
            for j in range(len(w1)):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break

        q = deque()
        for c in indegree.keys():
            if indegree[c] == 0:
                q.append(c)
        res = []
        while q:

            letter = q.popleft()
            print(q)
            res.append(letter)
            for i in adj[letter]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
        if len(res)!=len(indegree):
            return ""
        return "".join(res)
            

                    
        