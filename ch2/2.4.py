
class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def  add(self, value):
        added = Node(value, next=self.head)
        self.head = added


    def __str__(self):
        node = self.head
        out = []
        while (node != None):
            out += [str(node.value)]
            node = node.next

        return "->".join(out)

    def partition_list(self, pivot):

        node = self.head
        lhead, rhead = Node(999), Node(999)
        left = lhead
        right = rhead
        while (node != None):
            if node.value < pivot:
                left.next = Node(node.value)
                left = left.next
            else:
                right.next = Node(node.value)
                right = right.next
            node = node.next
        left.next = rhead.next
        self.head = lhead.next




input_list = LinkedList()
for v in [1,2,10,5,8,5,3]:
    input_list.add(v)

print("before", input_list)

input_list.partition_list(pivot=5)

print("after", input_list)
