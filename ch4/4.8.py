

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def post_explore(node, s, t):
    if (node != None):
        ls_is_desc, lt_is_desc, left_common  = post_explore(node.left, s, t)
        rs_is_desc, rt_is_desc, right_common = post_explore(node.right, s, t)

        if ls_is_desc | rs_is_desc: s_is_desc = True
        else: s_is_desc = False

        if lt_is_desc | rt_is_desc: t_is_desc = True
        else: t_is_desc = False

        common = None

        if left_common != None: common = left_common
        if right_common != None: common = right_common

        if s==node.value and t_is_desc == True:
            common = node.value

        if t==node.value and s_is_desc == True:
            common = node.value

        if s_is_desc == True and t_is_desc == True and common == None:
            common = node.value

        #print(node.value, ls_is_desc, lt_is_desc, rs_is_desc, rt_is_desc)
        #print("returning",s_is_desc | (s == node.value), t_is_desc | (t == node.value), common)
        return s_is_desc | (s == node.value), t_is_desc | (t == node.value), common

    else:
        return False, False, None


def first_common_ancestor(node, s, t):
    if s==t:
        return s

    return post_explore(node, s, t)[2]

root2 = Node(8, left=Node(4, left=Node(2), right=Node(12)),
            right = Node(10, right=Node(20)))

print(first_common_ancestor(root2, 10, 20), 10)
print(first_common_ancestor(root2, 2, 20), 8)
print(first_common_ancestor(root2, 2, 12), 4)
