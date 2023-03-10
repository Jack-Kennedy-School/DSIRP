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

def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

# Function to find priority
# of given operator.
def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0

# Function that converts infix
# expression to prefix expression.
def infixToPrefix(infix):
    # stack for operators.
    operators = []

    # stack for operands.
    operands = []

    for i in range(len(infix)):
        # If current character is an
        # opening bracket, then
        # push into the operators stack.
        if (infix[i] == '('):
            operators.append(infix[i])

        # If current character is a
        # closing bracket, then pop from
        # both stacks and push result
        # in operands stack until
        # matching opening bracket is
        # not found.
        elif (infix[i] == ')'):
            while (len(operators)!=0 and operators[-1] != '('):
                # operand 1
                op1 = operands[-1]
                operands.pop()

                # operand 2
                op2 = operands[-1]
                operands.pop()

                # operator
                op = operators[-1]
                operators.pop()

                # Add operands and operator
                # in form operator +
                # operand1 + operand2.
                tmp = op + op2 + op1
                operands.append(tmp)

            # Pop opening bracket
            # from stack.
            operators.pop()

        # If current character is an
        # operand then push it into
        # operands stack.
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")

        # If current character is an
        # operator, then push it into
        # operators stack after popping
        # high priority operators from
        # operators stack and pushing
        # result in operands stack.
        else:
            while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])

    # Pop operators from operators
    # stack until it is empty and
    # operation in add result of
    # each pop operands stack.
    while (len(operators)!=0):
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = op + op2 + op1
        operands.append(tmp)

    # Final prefix expression is
    # present in operands stack.
    return operands[-1]

class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        # This array is used a stack
        self.array = []

        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        # Pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        for ch in self.output:
            print(ch, end="")


if __name__ == "__main__":
    expression = input("Enter a mathematical infix expression: ")
    print(infixToPrefix(expression))
    obj = Conversion(len(expression))
    print(obj.infixToPostfix(expression))
    root = parse_expression(expression)
    turtle.hideturtle()
    turtle.speed(0)
    visualize_tree(root)
    turtle.mainloop()
