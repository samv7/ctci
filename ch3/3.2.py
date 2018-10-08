class Node(object):

    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)

class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, value):
        added = Node(value)
        added.next = self.head
        self.head = added

    def is_empty(self):
        return self.head == None

    def remove_last(self):
        if self.head != None:
            self.head = self.head.next
        else:
            return None

class Stack(object):

    def __init__(self):
        self.min = None
        self.prev_min = None
        self.items_list = LinkedList()
        self.min_list = LinkedList()


    def push(self, value):
        self.items_list.append(value)
        if self.min_list.is_empty() or value < self.min_list.head.value:
            self.min_list.append(value)

    def pop(self):

        last = self.items_list.head
        self.items_list.remove_last()

        if last != None:
            if self.min_list.head.value == last.value:
                self.min_list.remove_last()
            return last.value

        else:
            return None


    def min_value(self):
        if self.min_list.is_empty():
            return None
        else:
            return self.min_list.head.value

    def __str__(self):
        node = self.items_list.head

        output = []
        while (node != None):
            output += [str(node)]
            node = node.next
        return "->".join(output)


S = Stack()
input = [5,1,4,0,3,2]
for i in input:
    print("before adding: ",i,"min is",S.min_value())
    S.push(i)

print(S)

for i in input:
    print("popped",S.pop(),"now S looks like",S,"current min",S.min_value())
