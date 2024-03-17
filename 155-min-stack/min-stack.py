class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            cur_min = val
        else:
            cur_min = min(self.head.min, val)
        self.head = self.node(val, cur_min, self.head)

    def pop(self) -> None:
        if not self.head:
            return None
        else: 
            self.head = self.head.next

    def top(self) -> int:
        if not self.head:
            return None
        else:
            return self.head.val

    def getMin(self) -> int:
        if not self.head:
            return None
        else:
            return self.head.min

    class node:
        
        def __init__(self, val, min, next):
            self.val = val
            self.min = min
            self.next = next
