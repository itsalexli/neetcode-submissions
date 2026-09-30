class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "C" and stack:
                stack.pop()
            elif operation == "D" and stack:
                stack.append(int(stack[-1]) * 2)
            elif operation == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(operation)
        
        print(stack)
        total = 0
        for num in stack:
            total += int(num)
        return total
