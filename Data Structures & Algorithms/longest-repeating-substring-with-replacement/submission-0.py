class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxChar = ""
        maxNum = 0
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)  
            # Update maxNum and maxChar for current window
            if freq[s[r]] > maxNum:
                maxNum = freq[s[r]]
                maxChar = s[r]
            
            # Check if current window is valid
            window_size = r - l + 1
            if window_size - maxNum > k:
                # Shrink window from left
                freq[s[l]] -= 1
                l += 1
                # Recalculate maxNum for the new window
                maxNum = max(freq.values()) if freq else 0
            
            # Update result
            res = max(res, r - l + 1)
            
        return res