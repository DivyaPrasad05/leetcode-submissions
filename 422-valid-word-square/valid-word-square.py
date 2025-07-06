class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS = len(words)
        
        for i in range(ROWS):
            COLS = len(words[i])
            for j in range(COLS):
                if j >= ROWS or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False

        return True