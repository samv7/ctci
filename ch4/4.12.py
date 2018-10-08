


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)



def count_sums(node, target_sum, count=0, sums=[]):

    if (node != None):

        sums = [node.value]+[node.value + s for s in sums]

        l = count_sums(node.left, target_sum, count, sums)
        r = count_sums(node.right, target_sum, count, sums)

        count = sum([1 for x in sums if x==target_sum])
        return l+r+count
    else:
        return 0


T1 = Node(8, left=Node(2, left=Node(1), right=Node(5, left=Node(4))),
            right = Node(11))

print(count_sums(T1, target_sum=11))
