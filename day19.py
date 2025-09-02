def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit(): 
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
            else:
                raise ValueError(f"Unsupported operator: {token}")

    return stack[0]

print(evaluate_postfix("2 1 + 3 *"))
print(evaluate_postfix("5 6 +"))
print(evaluate_postfix("-5 6 -"))
print(evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))
print(evaluate_postfix("5"))

