class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def bst_status(node, called_by):
    if (node != None):
        lstatus, ldesc = bst_status(node.left, "left")
        rstatus, rdesc = bst_status(node.right, "right")

        status = True

        if (lstatus==False | rstatus==False):
            status = False

        if ldesc==None:
            ldesc = node.value
        else:
            if not (ldesc <= node.value):
                status = False

        if rdesc==None:
            rdesc = node.value
        else:
            if not ( node.value < rdesc):
                status = False

        if called_by=="left":
            desc = max(ldesc, rdesc)
        else:
            desc = min(ldesc, rdesc)


        return status, desc


    else:
        return True, None

def is_balanced(root):

    return bst_status(root, "left")


root1 = Node(8, left=Node(4, left=Node(2), right=Node(6)),
            right = Node(10, right=Node(20)))


root2 = Node(8, left=Node(4, left=Node(2), right=Node(12)),
            right = Node(10, right=Node(20)))



print(is_balanced(root1), True)

print(is_balanced(root2), False)
