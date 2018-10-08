import random
from collections import defaultdict


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.descendents = 0

    def __str__(self):
        return str(self.value)

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def __str__(self):

        return self.str_recurse(self.root)

    def str_recurse(self, node):

        if (node != None):

            l = self.str_recurse(node.left)
            r = self.str_recurse(node.right)

            return str(node)+"(d="+str(node.descendents)+") "+str(l)+" "+str(r)+" "
        else:
            return ""

    def insert(self, value):

        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_recurse(self.root, value)



    def insert_recurse(self, node, value):

        node.descendents += 1

        if node.left == None:
            node.left = Node(value)
            return
        else:
            if node.right == None:
                node.right = Node(value)
                return

            else:
                ldesc, rdesc = 0, 0
                if node.left != None: ldesc = node.left.descendents
                if node.right != None: rdesc = node.right.descendents
                if ldesc <= rdesc:
                    self.insert_recurse(node.left, value)
                else:
                    self.insert_recurse(node.right, value)

        return



    def get_random_node(self):

        r = random.uniform(0,1)

        return self.random_recurse(self.root, r, 0, 1)

    def random_recurse(self, node, r, lbound, rbound):

        if (node.left == None and node.right == None):
            return node

        if r <= lbound + 1/(node.descendents+1)*(rbound-lbound):
            return node
        else:
            lbound = 1/(node.descendents+1)

            if (node.left != None and node.right != None):
                D = node.left.descendents + node.right.descendents+2
                new_rbound = lbound + ((1+node.left.descendents)/D)*(rbound-lbound)

                if self.is_between(r, lbound, new_rbound):
                    return self.random_recurse(node.left, r, lbound, new_rbound)
                else:
                    return self.random_recurse(node.right, r, new_rbound, rbound)

            if (node.left != None and node.right == None):
                return self.random_recurse(node.left, r, lbound, rbound)


            if (node.left == None and node.right != None):
                return self.random_recurse(node.right, r, lbound, rbound)


    def is_between(self, v,a,b):
        if a<v and v<=b:
            return True
        else:
            return False


T = BinaryTree()

#for v in [1,2,3,4]:
for v in [8, 2, 1, 5, 4, 11]:
    T.insert(v)

print(T)

n = 1000000
hist = defaultdict(int)
for i in range(0,n):
    node = T.get_random_node()
    hist[node.value] += 1

hist = dict(zip(hist.keys(),[x/n for x in hist.values()]))

print(hist)
