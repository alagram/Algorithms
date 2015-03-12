
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

    # def pre_order(self):
    #     print(self.key)
    #     if self.left_child:
    #         self.left.pre_order()
    #     if self.right_child:
    #         self.right.pre_order()

# def build_tree():
#     tree = BinaryTree('a')

#     tree.insert_left('b')
#     tree.insert_right('c')
#     tree.get_left_child().insert_right('d')
#     tree.get_right_child().insert_left('e')
#     tree.get_right_child().insert_right('f')

#     return tree

# print(build_tree())

# r = BinaryTree('a')
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left('b')
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right('c')
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val('hello')
# print(r.get_right_child().get_root_val())
