"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格

"1 + 1"                2

" 2-1 + 2 "            3
"(1+(4+5+2)-3)+(6+8)"  23
"""
class Solution:
    def evaluate_expr(self, stack):
        res = stack.pop() if stack else 0
        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch.isdigit():
               operand = 10**n * int(ch) + operand
               n += 1
            elif ch == ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if ch =='(':
                    res = self.evaluate_expr(stack)
                    stack.append(res)
            else:
                stack.append(ch)
        if n:
            stack.append(operand)
        return self.evaluate_expr(stack)





