



class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_descendent(node):
    if (node != None):
        lmax = max_descendent(node.left)
        rmax = max_descendent(node.right)
        return max(lmax, rmax)
    else:
        return self.value

def min_descendent(node):
    if (node != None):
        lmin = min_descendent(node.left)
        rmin = min_descendent(node.right)
        return min(lmin, rmin)
    else:
        return self.value

def bst_status(node):
    if (node != None):
        lheight, lbalanced = bst_status(node.left)
        rheight, rbalanced = bst_status(node.right)

        if ( lbalanced==False | rbalanced == False):
            balanced = False
        else:
            if abs((1+lheight) - (1+rheight))>1:
                balanced = False
            else:
                balanced = True
        return max(lheight, rheight)+1, balanced
    else:
        return 0, True


def is_balanced(node):

    return bst_status(node)[1]


root1 = Node(8, left=Node(4, left=Node(2), right=Node(6)),
            right = Node(10, right=Node(20)))


root2 = Node(8, left=Node(4, left=Node(2), right=Node(12, right=Node(13))),
            right = Node(10))



print(bst_status(root1))

print(bst_status(root2))
