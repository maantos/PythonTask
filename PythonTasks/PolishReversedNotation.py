from collections import deque

from scapy.compat import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '/': lambda x, y: int(x/y),
              '*': lambda x, y: x * y}

        stack = []
        operands = "+-/*"

        for i in tokens:
            if i in operands and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                sum = op[i](num1,num2)
                stack.append(sum)
            else:
                stack.append(int(i))
        return stack.pop()

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))