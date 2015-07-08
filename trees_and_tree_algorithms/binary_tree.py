class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def pre_order(self):
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print self.key
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print self.key


def height(tree):
    if tree == None:
        return -1
    else:
        return 1 + max(height(tree.left_child), height(tree.right_child))


# def build_tree():
#     tree = BinaryTree('a')

#     tree.insert_left('b')
#     tree.insert_right('c')
#     tree.get_left_child().insert_left('d')
#     tree.get_left_child().insert_right('e')
#     tree.get_right_child().insert_left('f')
#     tree.get_right_child().insert_right('g')

#     return tree

# tree = build_tree()
# problem no. 8: http://cslibrary.stanford.edu/110/BinaryTrees.html
# http://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
def print_paths(node):
    return print_paths_recur(node, [])


def print_paths_recur(current_node, path):
    if current_node == None:
        return

    path.append(current_node.key)

    if current_node.left_child == None and current_node.right_child == None:
        for i in range(len(path)):
            print path[i]
        print "\n"
    else:
        print_paths_recur(current_node.left_child, path)
        print_paths_recur(current_node.right_child, path)
    path = path.pop(len(path)-1)

# O(n) time O(n) space
def iterative_post_order(root):
    s1 = []
    s2 = []
    s1.append(root)
    while s1 != []:
        root = s1.pop()
        s2.append(root)
        if root.get_left_child():
            s1.append(root.left_child)
        if root.get_right_child():
            s1.append(root.right_child)

    while s2 != []:
        root = s2.pop()
        print root.key

# O(n) time O(n) space
def iterative_inorder(root):
    if root == None:
        return

    stack = []

    while True:
        if root != None:
            stack.append(root)
            root = root.left_child
        else:
            if stack == []:
                break
            root = stack.pop()
            print root.key
            root = root.right_child
# print tree.post_order()
