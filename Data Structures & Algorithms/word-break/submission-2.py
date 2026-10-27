class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #iterating through s, we can keep going till we hit a match with a wordDict, when we do we have a choice, we can either choose the dictionary word or keep the word and hope to find a bigger thing, but we wont know until we've fully explored the path
        memo = {len(s):True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if s[i:i+len(w)] in wordDict:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
        