class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #conditions
        #1. curr power > left to buy (update max tokens)
        #2. update power = right if bought
        #3. keep a running curr tokens and max tokens
        #4. if equal to 0: update curr tokens 

        tokens.sort()
        print(tokens)
        l, r = 0, len(tokens) - 1
        points = 0
        max_points = 0
        while l <= r:
            while l <= r and power >= tokens[l]:
                points += 1
                max_points = max(points, max_points)
                power -= tokens[l]
                l += 1

            if points > 0:
                points -= 1
                power += tokens[r]
                r -= 1
            else:
                l += 1
        
            

        return max_points


        

            
        

            







    
