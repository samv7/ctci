


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

    def delete_mid(self, node):
        node.value = node.next.value
        node.next = node.next.next

    def get_node(self, value):
        node = self.head
        while (node != None):
            if (node.value == value):
                return node
            node = node.next
        return None

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

c_node = input_list.get_node('c')

input_list.delete_mid(c_node)

print("after", input_list)
