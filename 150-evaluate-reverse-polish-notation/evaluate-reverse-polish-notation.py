class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = { "*", "+", "/", "-" }
        s = []

        for t in tokens:
            res = 0
            if t not in operators:
                res = int(t)
            elif t == "*":
                res = s.pop() * s.pop()
            elif t == "+":
                res = s.pop() + s.pop()
            elif t == "-":
                res = -(s.pop())
                res += s.pop()
            else:
                op = s.pop()
                res = int(s.pop() / op)
            s.append(res)
            
        return s.pop()
