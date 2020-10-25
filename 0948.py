## 2020/10/25

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens: return 0
        tokens = sorted(tokens)
        score = 0
        start = 0
        end = len(tokens) - 1
        while start <= end:
            while start <= end and P >= tokens[start]:
                P -= tokens[start]
                start += 1
                score += 1
            if start < end and tokens[end] > tokens[start] and score > 0:
                P += tokens[end]
                end -= 1
                score -= 1
            else:
                break
        return score