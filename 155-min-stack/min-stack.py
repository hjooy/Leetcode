class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            cur_min = val
        else:
            cur_min = min(self.stack[-1][1], val)
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        if self.stack: self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
