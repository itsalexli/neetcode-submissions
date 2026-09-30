class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:  # Fix: handles negative numbers
                stack.append(int(token))  # Fix: convert to int immediately
            else:
                num2 = stack.pop()  # Already int, no conversion needed
                num1 = stack.pop()
                
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    # Fix: truncate toward zero for negative results
                    stack.append(int(num1 / num2))
        
        return stack[0]