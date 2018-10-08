class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self):
        return str(self.value)


def set_parent(node, parent):

    if (node != None):

        node.parent = parent
        set_parent(node.left, parent=node)
        set_parent(node.right, parent=node)

    else:
        pass

def find_node(node, target_value):

    if (node != None):
        if (node.value == target_value):
            return node
        l = find_node(node.left, target_value)
        r = find_node(node.right, target_value)
        if l!=None: return l
        if r!=None: return r
        return None
    else:
        return None


def find_successor(node):

    if node.right != None:
        return node.right

    return recurse(node.parent, called_by = node)

def recurse(node, called_by):

    if node.value == node.parent.value:
        if called_by.value == node.right.value:
            return None
        else:
            return node

    if called_by.value < node.value:
        return node.value
    else:
        return recurse(node.parent, called_by = node)

root1 = Node(8, left=Node(2, left=Node(1), right=Node(5)),
            right = Node(11) )

set_parent(root1, root1)

node = find_node(root1, target_value=2)
print("looking for 2", node.value)
print("2's successor: ", find_successor(node))
print("----------------------------------")
node = find_node(root1, target_value=5)
print("looking for 5", node.value)
print("5's successor: ", find_successor(node))
print("----------------------------------")
node = find_node(root1, target_value=8)
print("looking for 8", node.value)
print("8's successor: ", find_successor(node))
print("----------------------------------")
node = find_node(root1, target_value=11)
print("looking for 11", node.value)
print("11's successor: ", find_successor(node))
print("----------------------------------")
node = find_node(root1, target_value=1)
print("looking for 1", node.value)
print("1's successor: ", find_successor(node))
