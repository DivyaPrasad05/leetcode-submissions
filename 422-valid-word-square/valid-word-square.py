class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS = len(words)
        COLS = len(words[0])

        for i in range(ROWS):
            curr = words[i]
            colWord = ""
            for j in range(COLS):
                if j < ROWS and i < len(words[j]):
                    colWord += words[j][i]
            if colWord != curr:
                return False
        
        return True