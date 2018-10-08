
from collections import defaultdict


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_depths(root):

    depth_lists = defaultdict(list)
    depth_lists = depth_explore(root, 0, depth_lists)

    return depth_lists

def depth_explore(node, depth, depth_lists):

    if (node != None):
        #previsit
        depth_lists[depth].append(node.value)

        depth_lists = depth_explore(node.left, depth+1, depth_lists)
        depth_lists = depth_explore(node.right, depth+1, depth_lists)

        return depth_lists

    else:
        return depth_lists

root1 = Node(8, left=Node(4, left=Node(2), right=Node(6)),
            right = Node(10, right=Node(20)))


root2 = Node(8, left=Node(4, left=Node(2), right=Node(12, right=Node(13))),
            right = Node(10))

print(tree_depths(root1))
