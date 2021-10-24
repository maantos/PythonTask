from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result  = [0] * len(temperatures)
        size = len(temperatures)
        stack = deque()

        for i in range(size):
                while stack and stack[-1][0] < temperatures[i]:
                        temp, index = stack.pop()
                        result[index] = i - index
                stack.append((temperatures[i], i))
        return result









temperatures = [[73,74,75,71,69,72,76,73]]
                # [73,74,75,71,69,72,76,73],
                # [30,40,50,60],
                # [30,60,90]]

s = Solution()
for x in temperatures:

    print(s.dailyTemperatures(x))
#output [1,1,4,2,1,1,0,0]