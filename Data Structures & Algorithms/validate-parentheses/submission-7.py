class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)%2!=0:
            return False

        openToClose = {"(" : ")", "[" : "]", "{" : "}"}
        for c in s:
            if c in openToClose:
                stack.append(c)
            else:
                if stack and openToClose[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False




        
        
        