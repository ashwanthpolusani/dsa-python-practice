exp = "(a+b*c)/e-i+(j-f)"

def infix_to_postfix(exp):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = ""
    for ch in exp:
        if ch.isalnum():
            output += ch
        elif ch in precedence:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence[ch]):
                output += stack.pop()
            stack.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # Remove '('
    while stack:
        output += stack.pop()
    return output

def infix_to_prefix(exp):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    # Reverse the infix expression and swap '(' with ')'
    exp = exp[::-1]
    exp = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in exp])
    stack = []
    output = []
    for ch in exp:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    # Reverse output to get prefix
    return ' '.join(output[::-1])  # Added spaces between operators and operands

print(infix_to_postfix(exp))
print(infix_to_prefix(exp))
