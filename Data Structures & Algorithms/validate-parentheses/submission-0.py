class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif p == ')' or p == '}' or p == ']':
                if not stack:
                    return False
                top = stack[-1]
                if ((p==')' and top!='(') or
                    (p==']' and top!='[') or
                    (p=='}' and top!='{')):
                    return False
                stack.pop()
        return not stack


        