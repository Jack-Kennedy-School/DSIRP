class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def create_binary_tree(expression):
    root = None
    for char in expression:
        if char.isdigit():
            node = Node(char)
            insert(root, node)
        else:
            node = Node(char)
            node.right = root
            root = node
    return root

def postfix_traversal(node):
    result = []
    if node:
        result.extend(postfix_traversal(node.left))
        result.extend(postfix_traversal(node.right))
        result.append(node.value)
    return result

def postfix_expression(expression):
    tree = create_binary_tree(expression)
    print(''.join(postfix_traversal(tree)))

def prefix_traversal(node):
    result = []
    if node:
        result.append(node.value)
        result.extend(prefix_traversal(node.left))
        result.extend(prefix_traversal(node.right))
    return result

def prefix_expression(expression):
    tree = create_binary_tree(expression)
    print(''.join(prefix_traversal(tree)))


expression = input("enter an expression: ")
create_binary_tree(expression)
postfix_expression(expression)
prefix_expression(expression)
