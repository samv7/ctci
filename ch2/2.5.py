
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


    def __str__(self):
        node = self.head
        out = []
        while (node != None):
            out += [str(node.value)]
            node = node.next

        return "->".join(out)

def sum_lists(a, b):
    carry = 0
    out_tail = Node(999)
    out_head = out_tail

    lnode, rnode = a.head, b.head

    while (lnode != None and rnode != None):
        add = lnode.value + rnode.value

        out = Node(add + carry)

        if add > 9:
            carry = 1
            out.value = out.value - 10
        else:
            carry = 0


        lnode = lnode.next
        rnode = rnode.next
        out_tail.next = out
        out_tail = out_tail.next

    if lnode != None: node = lnode
    if rnode != None: node = rnode

    if node != None:
        while (node != None):
            out_tail.next = Node(node.value+carry)
            out_tail = out_tail.next
            carry = 0
            node = node.next


    output_list = LinkedList()
    output_list.head = out_head.next

    return output_list




x = LinkedList()
for v in [6,1,7]:
    x.add(v)


y = LinkedList()
for v in [2,9,5]:
    y.add(v)

print(x)
print(y)

print(sum_lists(x,y))

print("should be 912 or 2->1->9")

print("-----------------------")

x = LinkedList()
for v in [6,1,7,4]:
    x.add(v)


y = LinkedList()
for v in [2,9,5]:
    y.add(v)

print(x)
print(y)




print(sum_lists(x,y))
print(sum_lists(y,x))
print("should be 6469 or 9->6->4->6")

print("-----------------------")

x = LinkedList()
for v in [2,3,7,1,6]:
    x.add(v)


y = LinkedList()
for v in [9,2]:
    y.add(v)

print(x)
print(y)

print(sum_lists(x,y))
print(sum_lists(y,x))
print("should be 23808 or 8->0->8->3->2")
