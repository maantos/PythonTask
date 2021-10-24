class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        index = 0
        balance = True

        def matches(x, y):
            open = "({["
            close = ")}]"
            return open.index(x) == close.index(y)


        while index < len(s) and balance:
            x = s[index]
            if x in "({[":
                stack.append(x)
            else:
                if len(stack) is 0:
                    balance = False
                else:
                    top = stack.pop()
                    if not matches(top, x):
                        balance = False
            index += 1
        if len(stack) is 0 and balance:
            return True
        else:
            return False

s = Solution()
print(s.isValid("()"))