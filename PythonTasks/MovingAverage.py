# 346. Moving Average from Data Stream
from collections import deque


class MovingAverage:
    def __init(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        return window_sum / min(len(queue), size)


class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)


class MovingAverage3:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)



