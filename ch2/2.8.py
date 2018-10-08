from collections import defaultdict

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

    def find(self, value):
        node = self.head
        while (node != None):
            if (node.value == value):
                return node
            node = node.next
        return None

    def loop_node(self):

        visited = defaultdict(lambda *_: False)
        node = self.head

        while (node != None):
            visited[hash(node)] = True

            if node.next != None:
                if visited[hash(node.next)]:
                    return node
            node = node.next

        return None






input_list = LinkedList()
for v in [1,2,10,2,13,4]:
    input_list.add(v)

bad_node = input_list.find(value=2)
bad_node.next = input_list.find(value=13)

output = input_list.loop_node()
print(output.value)
