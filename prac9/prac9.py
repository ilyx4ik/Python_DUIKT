import sys
import re

def tokenize(expression: str) -> list:
    expression = expression.replace(" ", "")
    pattern = re.compile(r"(\d+\.?\d*|[\+\-\*\/\^\(\)])")
    tokens = pattern.findall(expression)
    
    reconstructed = "".join(tokens)
    if reconstructed != expression:
        raise ValueError("Невалідні символи у виразі")
    
    return tokens

def shunting_yard(tokens: list) -> list:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    associativity = {"+": "L", "-": "L", "*": "L", "/": "L", "^": "R"}
    output = []
    stack = []

    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] in precedence:
                op1 = token
                op2 = stack[-1]
                if (associativity[op1] == "L" and precedence[op1] <= precedence[op2]) or \
                   (associativity[op1] == "R" and precedence[op1] < precedence[op2]):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Незбалансовані дужки")
            stack.pop()
        else:
            raise ValueError(f"Невідомий оператор або символ: {token}")

    while stack:
        if stack[-1] in ["(", ")"]:
            raise ValueError("Незбалансовані дужки")
        output.append(stack.pop())

    return output

def evaluate_rpn(rpn_tokens: list) -> float:
    stack = []

    for token in rpn_tokens:
        if token.replace(".", "", 1).isdigit():
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise ValueError("Невалідний формат виразу")
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Ділення на нуль")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)

    if len(stack) != 1:
        raise ValueError("Невалідний формат виразу")
        
    return stack[0]

def calculate(expression: str) -> float:
    tokens = tokenize(expression)
    rpn = shunting_yard(tokens)
    return evaluate_rpn(rpn)

if __name__ == "__main__":
    try:
        expr = sys.stdin.read().strip()
        if not expr:
            print("Порожній ввід", file=sys.stderr)
            sys.exit(1)
        result = calculate(expr)
        print(result)
    except Exception as e:
        print(f"Помилка: {e}", file=sys.stderr)
        sys.exit(1)