class Solution:
    def numDecodings(self, s: str) -> int:
        #different decoding if starts with a 1, 2
        memo = {}
        #choose 1 or choose 2 digits
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            ways = dfs(i + 1)
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                ways += dfs(i + 2)
            
            memo[i] = ways
            return ways

        return dfs(0)
        



            

        
            
            


        