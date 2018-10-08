


class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None


    def add(self, value):
        added = Node(value, next=self.head)
        self.head = added

    def get_kthlast(self, k):

        node, counter = self.recurse(self.head, k)
        return node

    def recurse(self, node, k):

        if (node.next != None):
            cnode, counter = self.recurse(node.next, k)
            if counter == k:
                return cnode, k
            else:
                return node.value, counter+1
        else:
            return node.value, 1

    def __str__(self):
        node = self.head
        out = ""
        while (node != None):
            out += node.value
            node = node.next

        return out



input_list = LinkedList()
for ch in 'fedcba':
    input_list.add(ch)

print("before", input_list)

print("4th to last node is: ", input_list.get_kthlast(k=4))
