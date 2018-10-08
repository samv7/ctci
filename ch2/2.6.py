from math import floor

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

    def is_palindrome(self):

        if (self.head == None):
            return False

        if (self.head.next == None):
            return True

        node = self.head

        length = 0
        while (node != None):
            length += 1
            node = node.next



        stack = []
        node = self.head
        for i in range(0,floor(length/2)):
            stack.append(node.value)
            node = node.next

        if length%2==1:
            node = node.next #skip middle (irrelevant)

        while (node != None):
            if stack.pop() != node.value:
                return False
            node = node.next
        return True




input_list = LinkedList()
for v in [1,2,10,2,1]:
    input_list.add(v)

print("is this a palindrome?: ", input_list, input_list.is_palindrome())

input_list = LinkedList()
for v in [1,2,10,2,999]:
    input_list.add(v)

print("is this a palindrome?: ", input_list, input_list.is_palindrome())

input_list = LinkedList()
for v in [1,2,2,1]:
    input_list.add(v)

print("is this a palindrome?: ", input_list, input_list.is_palindrome())

input_list = LinkedList()
for v in [1,3]:
    input_list.add(v)

print("is this a palindrome?: ", input_list, input_list.is_palindrome())
