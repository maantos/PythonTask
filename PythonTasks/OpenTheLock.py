class Solution(object):
    def openLock(self, deadends, target):
        visited = set()
        step = 0
        que = []
        que.append("0000")
        visited.add("0000")
        while len(que) > 0:
            size = len(que)
            while size > 0:
                curr_position = que.pop()
                if curr_position.__eq__(target):
                    return step
                if curr_position in deadends:
                    size -= 1
                    continue
                for i in range(4):
                    x = curr_position[i]
                    s1 = curr_position[0:i] + ('0' if x.__eq__('9') else chr(ord(x) + 1)) + curr_position[i + 1:]
                    s2 = curr_position[0:i] + ('9' if x.__eq__('0') else chr(ord(x) - 1)) + curr_position[i + 1:]
                    if s1 not in visited and s1 not in deadends:
                        que.append(s1)
                        visited.add(s1)
                    if s2 not in visited and s2 not in deadends:
                        que.append(s2)
                        visited.add(s2)
                size -= 1
            step += 1
        return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
a = Solution()
#print(a.openLock(deadends, target))
b = set()
b.add((1,2))
c = (1,2)

print(*c)