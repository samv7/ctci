
class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)



def check_subtree(root1, T2):

    T1 = find(root1, target_value = T2.value)
    if T1 == None: return False

    return compare(T1, T2)


def compare(T1, T2):
    if (T1 != None):

        if T2==None:
            return False
        else:
            if T1.value != T2.value:
                return False

        l = compare(T1.left, T2.left)
        r = compare(T1.right, T2.right)
        return (l and r)
    else:
        if T2==None:
            return True
        else:
            return False


def find(node, target_value):
    if (node != None):
        if node.value == target_value:
            return node
        else:
            l = find(node.left, target_value)
            r = find(node.right, target_value)
            if l!=None: return l
            if r!=None: return r

            return None
    else:
        return None




T1 = Node(8, left=Node(4, left=Node(2), right=Node(6)),
            right = Node(10, right=Node(20)))

T2 = Node(4, left=Node(2), right=Node(6))
T3 = Node(4, left=Node(2), right=Node(7, left=Node(8)))

print(check_subtree(T1, T2))
print(check_subtree(T1, T3))
