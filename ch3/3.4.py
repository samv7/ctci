

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


class MyQueue(object):

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def __str__(self):
        output = ["---stack1---",str(self.stack_in),"---stack2---",
                    str(self.stack_out)]
        return "\n".join(output)

    def put(self, value):
        self.stack_in.push(value)

    def get(self):
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                return None
            else:
                while self.stack_in.is_empty() == False:
                    self.stack_out.push(self.stack_in.pop())

        return self.stack_out.pop()


Q = MyQueue()
for c in ['a','b','c']:
    Q.put(c)

print(Q)
print("after getting", Q.get())
print(Q)
print("adding 'd'",Q.put('d'))
print(Q)
print("after getting", Q.get())
print(Q)
print("after getting", Q.get())
print(Q)
print("after getting", Q.get())
print(Q)
