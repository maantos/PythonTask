from typing import List
from PythonTasks.Pythonds.Stack import Stack


class Solution:
    def reverseList1(self, x: str) -> None:
        if len(x) == 0:
            return x
        else:
            return self.reverseList1(x[1:]) + x[0]

    @staticmethod
    def reverseList2(x: List[str]) -> List[str]:
        if len(x) == 0:
            return
        else:
            return [a for a in x[::-1]]

    @staticmethod
    def reverseList3(x: List[str]) -> List[str]:
        s = Stack()
        for i in x:
            s.push(i)
        result = []
        while s.size() != 0:
            result.append(s.pop())
        return result



def main():
    justList = [str(x) for x in range(10)]
    p1 = Solution()
    print(p1.reverseList1("justList"))
    print(Solution.reverseList3(justList))
    #print(justList)
    # You cann add like this nice ... (76).__add__(1))


if __name__ == '__main__':
    main()
