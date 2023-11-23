class Solution:
    def isValid(self, s: str) -> bool:
        open_brakets = set( ['(', '{', '['] )
        stack = deque()
                      
        for c in s:
            if c in open_brakets:
                stack.append(c)
            elif stack:
                top = stack.pop()
                if c == ')' and top == '(':
                    continue
                elif c == ']' and top == '[':
                    continue
                elif c == '}' and top == '{':
                    continue
                return False
            else:
                return False
            
        if stack:
            return False
        
        return True