class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visit = set()

        wordList.append(beginWord)
        neighbours = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                pattern = wordList[i][:j] + "*" + wordList[i][j+1:]
                neighbours[pattern].append(wordList[i])
        words = 1
        visit = set([beginWord])
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return words
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in neighbours[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            words+=1
        return 0
        