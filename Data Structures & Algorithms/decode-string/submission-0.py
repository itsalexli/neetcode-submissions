class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = [] 
        num_stack = []
        curr = ""
        multiply = 0
        
        for char in s:
            if char.isdigit():
                multiply = multiply * 10 + int(char)
            elif char == "[":
                str_stack.append(curr)
                num_stack.append(multiply)
                curr = ""
                multiply = 0
            elif char == "]":
                temp = curr
                curr = str_stack.pop()
                count = num_stack.pop()
                curr += temp * count
            else:
                curr += char
        
        return curr

# multiply 2
# curr 
#num_stack
#curr_stack ""



      
