class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
                
            if not char.isdigit():
                stack.append(char)
                
        return ''.join(stack)

        