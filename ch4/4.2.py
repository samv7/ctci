from math import floor


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, node, value):

        if (node != None):
            if value <= node.value:
                if node.left == None:
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            if value > node.value:
                if node.right == None:
                    node.right = Node(value)
                else:
                    self.insert(node.right, value),
        else:
            pass


def post_order(node):
    return post_explore(node)

def post_explore(node):

    if (node != None):
        l = post_explore(node.left)
        r = post_explore(node.right)
        return " ".join([l, r, str(node.value)])
    else:
        return ""

def min_bst(input):

    L = len(input)
    med = floor(L/2)

    root = Node(value = input[med])
    recurse(input[0:(med)], root)
    recurse(input[(med+1):], root)

    return root

def recurse(input, node):

    if len(input)<=1:
        if len(input)==0:
            pass
        else:
            node.insert(node, input[0])
    else:
        L = len(input)
        med = floor(L/2)
        node.insert(node, input[med])

        recurse(input[0:(med)], node)
        recurse(input[(med+1):], node)

root = min_bst([1,2,5,8,11])
print(post_order(root))
