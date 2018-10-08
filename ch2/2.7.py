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

    def get_node(self, value):
        node = self.head
        while (node != None):
            if (node.value == value):
                return node
            node = node.next
        return None

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

def find_intersection(list1, list2):

    node = list1.head
    l_len = 0
    while (node != None):
        ltail = node
        l_len += 1
        node = node.next

    node = list2.head
    r_len = 0
    while (node != None):
        rtail = node
        r_len += 1
        node = node.next

    if hash(ltail) == hash(rtail):
        pass
    else:
        return None

    lnode = list1.head
    rnode = list2.head

    if l_len != r_len:
        if l_len > r_len:
            for i in range(0,l_len - r_len):
                lnode = lnode.next
        else:
            for i in range(0,r_len - l_len):
                rnode = rnode.next

    while (lnode != None):

        if hash(lnode)==hash(rnode):
            return lnode

        lnode = lnode.next
        rnode = rnode.next




def does_intersect_byhash(list1, list2):

    lnode = list1.head
    rnode = list2.head

    visitedl = defaultdict(lambda *_: False)
    visitedr = defaultdict(lambda *_: False)

    while (lnode == None and rnode == None)==False:

        if lnode != None:
            visitedl[hash(lnode)] = True
            if visitedr[lnode]:
                return True

            lnode = lnode.next
        if rnode != None:
            visitedr[hash(rnode)] = True
            if visitedl[hash(rnode)]:
                return True
            rnode = rnode.next


    return False



list1 = LinkedList()
for v in [1,2,10,2,13,4]:
    list1.add(v)



list2 = LinkedList()
for v in [4,5,9]:
    list2.add(v)

print("before: does intersect?", find_intersection(list1, list2))

lnode = list1.find(13)
rnode = list2.find(9)

rnode.next = lnode


print("after: does intersect?", find_intersection(list1, list2).value)
