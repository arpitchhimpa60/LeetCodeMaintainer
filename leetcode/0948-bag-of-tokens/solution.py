# Runtime: 3 ms
# Memory: 19.1 MB

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        score = 0
        maxi = 0
        i = 0
        j = len(tokens)-1
        while i<=j:
            if power >= tokens[i]:
                power-=tokens[i]
                score+=1
                i+=1
            else:
                if score >= 1:
                    power+=tokens[j]
                    score-=1
                    j-=1
                else:
                    break
            maxi = max(score,maxi)
        return maxi
        