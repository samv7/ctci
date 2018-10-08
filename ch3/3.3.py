

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        added = Node(value)
        added.next = self.head
        self.head = added

    def remove_last(self):
        if self.head != None:
            self.head = self.head.next

    def __str__(self):
        node = self.head

        output = []
        while (node != None):
            output += [str(node)]
            node = node.next
        return "->".join(output)

class Stack(object):

    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.head == None

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            last = self.items.head
            self.items.remove_last()
            return last

    def __str__(self):
        return str(self.items)

class StackOfStacks(object):

    def __init__(self, capacity):
        self.stacks = LinkedList()
        self.stacks.append(Stack())
        self.capacity = capacity
        self.cur_size = 0

    def push(self, value):
        if self.cur_size >= self.capacity:
            self.stacks.append(Stack())
            self.cur_size = 0

        self.stacks.head.value.push(value)
        self.cur_size += 1

    def pop(self):
        if self.cur_size == 0:
            self.stacks.remove_last()
            if self.stacks.head == None:
                self.cur_size = 0
                return None
            else:
                self.cur_size = self.capacity
        self.cur_size -= 1
        return self.stacks.head.value.pop()

    def __str__(self):
        node = self.stacks.head
        if node==None: return None

        output = []
        i = 1
        while (node != None):
            output.append("---Stack "+str(i)+"---")
            output.append(str(node.value))
            output.append("--------------")
            node = node.next
            i += 1
        return "\n".join(output)

S = StackOfStacks(capacity = 3)
input = list(range(1,11))
for i in input:
    S.push(i)
    print("After pushing: ",i)
    print(S)


for i in input:
    print("After popping: ", S.pop())
    print(S)
