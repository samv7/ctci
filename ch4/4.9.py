

class Node(object):

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def bst_sequences(node, upseq = [[]]):

    lupseq, rupseq = [], []
    if node.left != None:
        lupseq = [s + [node.left.value] for s in upseq]:
        if node.right != None:
            lupseq = [s + [node.right.value] for s in lupseq]

    if node.right != None:
        rupseq = [s + [node.right.value] for s in upseq]:
        if node.left != None:
            rupseq = [s + [node.left.value] for s in rupseq]


    lseqs = bst_sequences(node.left, lupseq + rupseq)
    rseqs = bst_sequences(node.right, lupseq + rupseq)


root1 = Node(8, left=Node(4, left=Node(2), right=Node(6)),
            right = Node(10, right=Node(20)))
