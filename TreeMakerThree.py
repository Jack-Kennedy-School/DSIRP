import operator
import re
import turtle

# Define the precedence and associativity of each operator
operators = {
    "+": (1, operator.add),
    "-": (1, operator.sub),
    "*": (2, operator.mul),
    "/": (2, operator.truediv),
    "^": (3, operator.pow)
}

# Define a regular expression to match valid tokens in the input expression
token_pattern = re.compile(r"([\d\.]+|\(|\)|\+|\-|\*|/|\^)")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

def parse_expression(expression):
    tokens = list(re.findall(token_pattern, expression))
    return parse_expression_helper(tokens)

def parse_expression_helper(tokens):
    # First, parse the left operand
    if tokens[0] == "(":
        # If the left operand is enclosed in parentheses, recursively parse the expression inside the parentheses
        tokens.pop(0)
        left = parse_expression_helper(tokens)
        tokens.pop(0)  # Consume the closing parenthesis
    else:
        # Otherwise, parse the next token as a number
        left = Node(float(tokens.pop(0)))

    # If there are no more tokens, we're done parsing
    if not tokens:
        return left

    # Otherwise, parse the operator and the right operand recursively
    while tokens:
        op_token = tokens[0]
        if op_token == ")":
            return left
        op_info = operators[op_token]
        if op_info[0] <= operators.get(tokens[1], (0,))[0]:
            right = parse_expression_helper(tokens[2:])
        else:
            tokens.pop(0)
            right = parse_expression_helper(tokens)
        # Create a new node for the operator and link it to the left and right operands
        node = Node(op_info[1])
        node.left = left
        node.right = right
        left = node
    return left

def visualize_tree(node, x=0, y=turtle.window_height() / 2, dx=50, dy=50):
    if node.left:
        visualize_tree(node.left, x - dx, y - dy, dx, dy * 1.2)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x - dx, y - dy)
    if node.right:
        visualize_tree(node.right, x + dx, y - dy, dx, dy * 1.2)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + dx, y - dy)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(str(node.value.__name__ if callable(node.value) else node.value), align="center", font=("Arial", 14, "normal"))



if __name__ == "__main__":
    expression = input("Enter a mathematical infix expression: ")
    root = parse_expression(expression)
    turtle.hideturtle()
    turtle.speed(0)
    visualize_tree(root)
    turtle.mainloop()
