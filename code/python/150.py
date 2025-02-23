# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                    continue
                case '*':
                    stack.append(stack.pop() * stack.pop())
                    continue
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                    continue
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
                    continue
                case _:
                    stack.append(int(token))
        return stack.pop()
