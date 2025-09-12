class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo = None) -> bool:
        if memo == None:
            memo = {}
        if s in memo:
            return memo[s]
        if s == '':
            return True
        
        for word in wordDict:
            if s.startswith(word): # prefix
                suffix = s[len(word):]
                if self.wordBreak(suffix, wordDict, memo) == True:
                    memo[s] = True
                    return True

        memo[s] = False
        return False
