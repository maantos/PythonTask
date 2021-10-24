# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
INF = 2147483647

def WallsAndGate(rooms):
    print(len(rooms))
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                visit(i, j, rooms, 0)

def visit(x, y, rooms, count):
    if 0 > x or x >= len(rooms) or 0 > y or y >= len(rooms[0]) or rooms[x][y] < count:
        return

    rooms[x][y] = count
    visit(x + 1, y, rooms, count + 1)
    visit(x - 1, y, rooms, count + 1)
    visit(x, y + 1, rooms, count + 1)
    visit(x, y - 1, rooms, count + 1)


rooms = [[INF, -1, 0, INF],
         [INF, INF, INF, -1],
         [INF, -1, INF, -1],
         [0, -1, INF, INF]]

a = []
a.append([1,2])
x,y = a.pop()
print(y)