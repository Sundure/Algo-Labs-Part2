from __future__ import annotations
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

class Lab4:

    class RedBlackTree:
        def __init__(self,value=None,root = None,left=None,right=None) -> None:
            self.value = value
            self.root = root
            if root == None or value == None:
                self.color = Color.BLACK
            else:
                self.color = Color.RED
            
            if value == None:
                return

            if left == None:
                self.left = Lab4.RedBlackTree(root=self)
            else:
                self.left = left

            if right == None:
                self.right= Lab4.RedBlackTree(root=self)
            else:
                self.right= right
        
        def add_element(self, node: Lab4.RedBlackTree) -> None:
            current_node = self
            previus_node = None
            while True:
                if current_node.value != None and node.value <= current_node.value:
                    previus_node = current_node
                    current_node = current_node.left
                elif current_node.value != None and node.value > current_node.value:
                    previus_node = current_node
                    current_node = current_node.right
                else:
                    if node.value <= previus_node.value:
                        previus_node.left = Lab4.RedBlackTree(node.value, previus_node)
                    elif node.value > previus_node.value:
                        previus_node.right = Lab4.RedBlackTree(node.value, previus_node)
                    break
        
        @staticmethod
        def recolor(node: Lab4.RedBlackTree):
            chosen_node = node
            while chosen_node.root != None and chosen_node.root.root != None and chosen_node.root.root.left.color != Color.BLACK and chosen_node.root.root.right.color != Color.BLACK:
                grandfather = chosen_node.root.root
                if grandfather.root != None:
                    grandfather.color = Color.RED
                grandfather.left.color = Color.BLACK
                grandfather.right.color = Color.BLACK
                chosen_node = grandfather

        def rotate_left(self):
            chosen_node: Lab4.RedBlackTree = self
            while chosen_node.root != None:
                chosen_node = chosen_node.root 

            tree_root: Lab4.RedBlackTree = chosen_node
            buffer: Lab4.RedBlackTree

            if tree_root.value == None:
                return

            right_node = self.right
            self.right = right_node.left
            if right_node.left.value != None:
                right_node.left.root = self
            right_node.root = self.root
            if self.root == None:
                pass
            elif self == self.root.left:
                self.root.left = right_node
            else:
                self.root.right = right_node
            right_node.left = self
            self.root = right_node

        def rotate_right(self):
            left_node = self.left
            self.left = left_node.right
            if left_node.right.value != None:
                left_node.right.root = self
            left_node.root = self.root
            if self.root == None:
                pass
            elif self == self.root.right:
                self.root.right = left_node
            else:
                self.root.left = left_node
            left_node.right = self
            self.root = left_node

        def fix_insert(self):
            node = self
            while node.root != None and node.root.color == Color.RED:
                if node.root == node.root.root.left:
                    uncle = node.root.root.right
                    if uncle.value != None and uncle.color == Color.RED:
                        node.root.color = Color.BLACK
                        uncle.color = Color.BLACK
                        node.root.root.color = Color.RED
                        node = node.root.root
                    else:
                        if node == node.root.right:
                            node = node.root
                            node.rotate_left()
                        node.root.color = Color.BLACK
                        node.root.root.color = Color.RED
                        node.root.root.rotate_right()
                else:
                    uncle = node.root.root.left
                    if uncle.value != None and uncle.color == Color.RED:
                        node.root.color = Color.BLACK
                        uncle.color = Color.BLACK
                        node.root.root.color = Color.RED
                        node = node.root.root
                    else:
                        if node == node.root.left:
                            node = node.root
                            node.rotate_right()
                        node.root.color = Color.BLACK
                        node.root.root.color = Color.RED
                        node.root.root.rotate_left()
            while node.root != None:
                node = node.root
            node.color = Color.BLACK

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __le__(self, other):
        return self.priority >= other.priority

    def __gt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.tree = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        tree_node = Lab4.RedBlackTree(value=new_node)
        if self.tree == None or self.tree.value == None:
            self.tree = tree_node
            self.tree.color = Color.BLACK
        else:
            self.tree.add_element(tree_node)
            curr = self.tree
            while True:
                if new_node <= curr.value:
                    if curr.left.value == new_node and curr.left.left.value == None and curr.left.right.value == None:
                        curr.left.color = Color.RED
                        curr.left.fix_insert()
                        break
                    curr = curr.left
                else:
                    if curr.right.value == new_node and curr.right.left.value == None and curr.right.right.value == None:
                        curr.right.color = Color.RED
                        curr.right.fix_insert()
                        break
                    curr = curr.right
            while self.tree.root != None:
                self.tree = self.tree.root

    def peek(self):
        if self.tree == None or self.tree.value == None:
            return None
        curr = self.tree
        while curr.left.value != None:
            curr = curr.left
        return curr.value

    def pop(self):
        if self.tree == None or self.tree.value == None:
            return None
        curr = self.tree
        while curr.left.value != None:
            curr = curr.left
        
        res = curr.value
        
        if curr.right.value != None:
            curr.value = curr.right.value
            curr.left = curr.right.left
            if curr.left.value != None:
                curr.left.root = curr
            curr.right = curr.right.right
            if curr.right.value != None:
                curr.right.root = curr
        else:
            curr.value = None
            curr.left = None
            curr.right = None
        
        return res

test = Lab4.RedBlackTree(value=10)
