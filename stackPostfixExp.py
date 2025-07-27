def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        elif char in "+-*/":
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

def infix_to_prefix(expression):
    stack = []
    prefix = []
    for char in expression[::-1]:
        if char.isalnum():
            prefix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            if stack and stack[-1] == ')':
                stack.pop()
        elif char in "+-*/":
            while stack and precedence(stack[-1]) > precedence(char):
                prefix.append(stack.pop())
            stack.append(char)
    while stack:
        prefix.append(stack.pop())
    return ''.join(prefix[::-1])

def post_pre_to_infix(expression , type):
    stack = []
    expression = expression[::-1] if type == 'prefix' else expression
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if type == 'postfix':
                stack.append(f'({op2}{char}{op1})')
            elif type == 'prefix':
                stack.append(f'({op1}{char}{op2})')
            else:
                raise ValueError("Invalid type: must be 'postfix' or 'prefix'")
    return stack[0]

if __name__ == "__main__":
    expression = input("Enter a infix expression: ")
    postfix = infix_to_postfix(expression)
    print("Obtained expression Postf : ", postfix)
    prefix = infix_to_prefix(expression)
    print("Obtained expression Pref : ", prefix)
    finalInf = post_pre_to_infix(postfix, 'postfix')
    print("Obtained expression Infix from Postf : ", finalInf)
    finalInf = post_pre_to_infix(prefix, 'prefix')
    print("Obtained expression Infix from Pref : ", finalInf)
