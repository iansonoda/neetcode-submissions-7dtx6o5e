class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators and len(numStack) >= 2:
                num1 = numStack.pop()
                num2 = numStack.pop()
                
                if token == '+':
                    res = num1 + num2

                elif token == '-':
                    res = num2 - num1

                elif token == '*':
                    res = num1 * num2

                else:
                    res = int(num2 / num1)

                numStack.append(res)
            else:
                numStack.append(int(token))

        return numStack[-1]