from collections import defaultdict

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

    def remove_dups(self):
        visited = defaultdict(lambda *_: False)
        node = self.head
        prev = None
        while (node != None):
            if visited[node.value]:
                if node.next == None:
                    prev.next = None
                    node = None
                else:
                    node.value = node.next.value
                    node.next = node.next.next
                    prev = node
                    node = node.next
            else:
                visited[node.value] = True
                prev = node
                node = node.next



    def __str__(self):
        node = self.head
        out = []
        while (node != None):
            out += [str(node.value)]
            node = node.next

        return "->".join(out)



input_list = LinkedList()
for v in [1,2,10,5,8,5,3]:
    input_list.add(v)

print("before", input_list)

input_list.remove_dups()

print("after", input_list)


input_list = LinkedList()
for v in [1,2,10,5,8,5,1]:
    input_list.add(v)

print("before", input_list)

input_list.remove_dups()

print("after", input_list)
