import unittest

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from trees_and_tree_algorithms import binary_search_tree



class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = binary_search_tree.BinarySearchTree()

    def test_get_put(self):
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')

        assert self.bst.get(50) == 'a'
        assert self.bst.get(45) == 'f'
        assert self.bst.get(85) == 'd'
        assert self.bst.get(10) == 'b'
        assert self.bst.root.key == 50
        assert self.bst.root.left_child.key == 10
        assert self.bst.root.right_child.key == 70


if __name__ == '__main__':
    unittest.main()
