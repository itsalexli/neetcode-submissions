class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart, resLen = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # loop overshoots by one on each side
            return l + 1, r - l - 1  # start, length

        for i in range(len(s)):
            # odd palindrome: center is one char
            start, length = expand(i, i)
            if length > resLen:
                resStart, resLen = start, length

            # even palindrome: center is between two chars
            start, length = expand(i, i + 1)
            if length > resLen:
                resStart, resLen = start, length

        return s[resStart: resStart + resLen]