from dataclasses import dataclass
from abc import ABCMeta
from typing import List, Optional, Tuple
from typing_extensions import ParamSpec
import solutions.y2021.lib2021
import math

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict

# Math homework
# Pairs
# Addition -> [1,2] + [3,4] = [[1,2],[3,4]]
# Must be reduced
# Explode -> if nested in 4 pairs, left most explodes
# Splits -> if regular number is 10 or more, left most splits
# Explode -> left to left regular number (not pair), right to right regular number
# Exploding pairs are always 2 regular numbers
# Split -> replace it with a pair, left is number / 2 FLOORED, right is number / 2 CEILED
# Input is a list of snailfish numbers that need to be added
# Reduce after each addition
# Get magnitude of the sum
# Magnitude is 3 * left, 2 * right, of a regular number its just the number


class TreeNode():
    depth: int
    parent: Optional['Pair']

    def __init__(self, depth: int) -> None:
        self.depth = depth
        self.parent: Optional['Pair'] = None

    def get_magnitude(self):
        pass

    def should_explode(self):
        pass

    def execute_explode(self):
        pass

    def execute_split(self):
        pass

    def incement_depth(self):
        pass

    def __add__(self, other: 'TreeNode'):
        if not isinstance(other, TreeNode):
            raise Exception()

        self.incement_depth()
        other.incement_depth()

        return Pair(self, other, 0)

    def reduce_action(self):
        if self.execute_explode():
            print('Exploded')
            return True
        elif self.execute_split():
            print('splitted')
            return True
        else:
            return False

    def reduce_fully(self):
        while self.reduce_action():
            print(self)


class Number(TreeNode):
    number: int

    def __init__(self, number: int, depth: int) -> None:
        super().__init__(depth)

        self.number = number

        # print(f'Creating Number with depth {self.depth}')

    def get_magnitude(self):
        return self.number

    def should_explode(self):
        return False

    def execute_split(self):
        if self.number >= 10:
            pair = Pair(Number(math.floor(self.number / 2), self.depth + 1),
                        Number(math.ceil(self.number / 2), self.depth + 1),
                        self.depth)
            pair.left.parent = pair
            pair.right.parent = pair
            self.parent.request_replacement(self, pair)
            return True
        else:
            return False

    def incement_depth(self):
        self.depth += 1

    def __str__(self) -> str:
        return f'({self.depth}|{1 if self.parent else 0}|{self.number})'


class Pair(TreeNode):
    left: TreeNode
    right: TreeNode

    def __init__(self,
                 left: TreeNode,
                 right: TreeNode,
                 depth: int) -> None:
        super().__init__(depth)

        self.left = left
        self.right = right

        # print(f'Creating Pair with depth {self.depth}')

    def get_magnitude(self):
        return 3 * self.left.get_magnitude() + 2 * self.right.get_magnitude()

    def should_explode(self):
        return self.depth == 4

    def execute_explode(self):
        if self.should_explode():
            print(f'exploding {self}')
            if not isinstance(self.left, Number) or not isinstance(self.right, Number):
                raise Exception()
            left_add = self.left.number
            right_add = self.right.number

            left_worked = self.parent.add_to_most_right_left(self, left_add)
            right_worked = self.parent.add_to_most_left_right(self, right_add)

            self.parent.request_removal(self, left_worked, right_worked)
            return True
        else:
            if self.left.execute_explode():
                return True
            elif self.right.execute_explode():
                return True
            else:
                return False

    def add_to_most_right_left(self, child_asking: 'Pair', number: int) -> bool:
        # Right is asking to put left, then put left right*
        # Left is asking to put left, then up up up.
        if self.left == child_asking:
            if self.parent != None:
                self.parent.add_to_most_right_left(self, number)
            else:
                return False
        else:
            child = self.left
            while isinstance(child, Pair):
                child = child.right
            if isinstance(child, Number):
                child.number += number
                return True
            else:
                raise Exception()

    def add_to_most_left_right(self, child_asking: 'Pair', number: int) -> bool:
        if self.right == child_asking:
            if self.parent != None:
                self.parent.add_to_most_left_right(self, number)
            else:
                return False
        else:
            child = self.right
            while isinstance(child, Pair):
                child = child.left
            if isinstance(child, Number):
                child.number += number
                return True
            else:
                raise Exception()

    def request_removal(self, child: 'Pair', left_worked, right_worked):
        if self.left == child:
            self.left = Number(0, self.depth + 1)
            self.left.parent = self
        elif self.right == child:
            self.right = Number(0, self.depth + 1)
            self.right.parent = self

    def request_replacement(self, child: TreeNode, replace_with: TreeNode):
        replace_with.parent = self
        if self.left == child:
            self.left = replace_with
        elif self.right == child:
            self.right = replace_with

    def execute_split(self):
        if self.left.execute_split():
            return True
        elif self.right.execute_split():
            return True
        else:
            return False

    def incement_depth(self):
        self.depth += 1

        self.left.incement_depth()
        self.right.incement_depth()

    def __str__(self) -> str:
        return f'[{self.depth} {1 if self.parent else 0} > {self.left},{self.right}]'


@input_strings
def p1(lines) -> str:
    trees: List[TreeNode] = []
    lines = '''
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
'''.split()
    # lines = [lines[0]]
    for line in lines:
        # line = '[[[[[9,8],1],2],3],4]'
        depth = 0
        tree_node_stack: List[TreeNode] = []
        for i, char in enumerate(line):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
                right = tree_node_stack.pop()
                left = tree_node_stack.pop()
                pair = Pair(left, right, depth)
                left.parent = pair
                right.parent = pair
                tree_node_stack.append(pair)
            elif char == ',':
                pass
            else:
                tree_node_stack.append(Number(int(char), depth))
        if len(tree_node_stack) != 1:
            raise Exception()
        trees.append(tree_node_stack[0])
        print('Constructed')

    tree = trees[0]
    tree.reduce_fully()
    print(tree)
    for other_tree in trees[1:]:
        tree += other_tree
        tree.reduce_fully()
    
    print(tree)

    return tree.get_magnitude()


def p2(input_data) -> str:
    pass
