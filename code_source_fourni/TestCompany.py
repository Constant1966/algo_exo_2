import random
# import collections

from BinarySearchTree import BinarySearchTree
from TestHelper import TestHelper

class TestBinary:
    def test(self):
        self.test_random()
        self.test_random_contains()
        self.test_random_not_contains()
        self.test_with_one_value()
        self.test_with_right_values()
        self.test_with_left_values()
        self.test_height_zero()
        self.test_height_random()
        self.test_height_one_side()
        self.test_complexity()
        self.test_contains_complexity()
        self.test_height_complexity()

    def test_random(self):
        max_val = 1000
        tree = BinarySearchTree(max_val // 2)
        lst = [max_val // 2]
        for _ in range(max_val):
            next_val = random.randint(0, max_val)
            tree.insert(next_val)
            lst.append(next_val)
        lst.sort()
        in_order = tree.toStringInOrder()
        sorted_array = str(lst)
        TestHelper.printTest(in_order == sorted_array)

    def test_random_contains(self):
        max_val = 1000
        tree = BinarySearchTree(max_val // 2)
        lst = [max_val // 2]
        for _ in range(max_val):
            next_val = random.randint(0, max_val)
            tree.insert(next_val)
            lst.append(next_val)
        rand_int = random.choice(lst)
        TestHelper.printTest(tree.contains(rand_int))

    def test_random_not_contains(self):
        max_val = 1000
        tree = BinarySearchTree(max_val // 2)
        for _ in range(max_val):
            next_val = random.randint(0, max_val)
            tree.insert(next_val)
        TestHelper.printTest(not tree.contains(max_val))

    def test_with_one_value(self):
        next_val = random.randint(0, 1000)
        tree = BinarySearchTree(next_val)
        lst = [next_val]
        in_order = tree.toStringInOrder()
        sorted_array = str(lst)
        TestHelper.printTest(in_order == sorted_array)

    def test_with_right_values(self):
        max_val = 1000
        tree = BinarySearchTree(0)
        lst = [0]
        for i in range(1, max_val):
            tree.insert(i)
            lst.append(i)
        lst.sort()
        in_order = tree.toStringInOrder()
        sorted_array = str(lst)
        TestHelper.printTest(in_order == sorted_array)

    def test_with_left_values(self):
        max_val = 1000
        tree = BinarySearchTree(1000)
        lst = [1000]
        for i in range(999, -1, -1):
            tree.insert(i)
            lst.append(i)
        lst.sort()
        in_order = tree.toStringInOrder()
        sorted_array = str(lst)
        TestHelper.printTest(in_order == sorted_array)

    def test_height_zero(self):
        tree = BinarySearchTree(10)
        TestHelper.printTest(tree.getHeight() == 0)

    def test_height_random(self):
        tree = BinarySearchTree(10)
        for val in [8, 8, 9, 12, 15, 14, 14, 15, 15]:
            tree.insert(val)
        TestHelper.printTest(tree.getHeight() == 5)

    def test_height_one_side(self):
        max_val = 1000
        tree = BinarySearchTree(0)
        for i in range(1, max_val):
            tree.insert(i)
        TestHelper.printTest(tree.getHeight() == max_val - 1)

    def test_complexity(self):
        max_val = 2000
        is_good = True
        for _ in range(max_val):
            tree = BinarySearchTree(max_val // 2)
            lst = [max_val // 2]
            for _ in range(max_val):
                next_val = random.randint(0, max_val)
                tree.insert(next_val)
                lst.append(next_val)
            lst.sort()
            in_order = tree.toStringInOrder()
            sorted_array = str(lst)
            is_good &= in_order == sorted_array
        TestHelper.printTest(is_good)

    def test_contains_complexity(self):
        max_val = 2000
        is_good = True
        for _ in range(max_val):
            tree = BinarySearchTree(max_val // 2)
            lst = [max_val // 2]
            for _ in range(max_val):
                next_val = random.randint(0, max_val)
                tree.insert(next_val)
                lst.append(next_val)
            rand_int = random.choice(lst)
            is_good &= tree.contains(rand_int)
        TestHelper.printTest(is_good)

    def test_height_complexity(self):
        max_val = 1000
        is_good = True
        for _ in range(max_val):
            tree = BinarySearchTree(0)
            for i in range(1, max_val):
                tree.insert(i)
            is_good &= tree.getHeight() == max_val - 1
        TestHelper.printTest(is_good)
