class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                wildCardWord = word[:j] + "*" + word[j+1:]
                adj[wildCardWord].append(word)

        visit = set()
        q = deque()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if endWord == word:
                    return res
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res+=1
        return 0
        