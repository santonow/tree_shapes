from copy import deepcopy
import sys

"""Print all rooted unlabeled binary trees with given number of leafs.

The trees are printed in Newick format.
"""


class Leaf:
    """A class representing a leaf."""

    def __init__(self):
        """Initialize parameters."""
        self.is_leaf = True

    def __str__(self):
        return ""

    def __eq__(self, other):
        return isinstance(other, Leaf)

    def __ne__(self, other):
        return not self == other

    def __iter__(self):
        yield self

    def __repr__(self):
        return "Leaf()"

    def __hash__(self):
        return hash(repr(self))


class Node:
    def __init__(self, left=None, right=None, root=False):
        self.is_leaf = False
        self.left = left
        self.right = right
        self.root = root

    def __eq__(self, other):
        """Check if two trees are equal.

        We can just compare sets of each node's children.
        Together with __hash__ allows putting Node object in sets.
        """
        if not isinstance(other, Node):
            return False
        return {self.left, self.right} == {other.left, other.right}

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        """Newick trees end with semicolons."""
        if self.root:
            return f"({str(self.left)},{str(self.right)});"
        else:
            return f"({str(self.left)},{str(self.right)})"

    def __iter__(self):
        """Iterate over nodes and leafs of a tree."""
        yield self
        yield from self.left
        yield from self.right

    def __repr__(self):
        return f"Node({repr(self.left)},{repr(self.right)}, root={self.root})"

    def __hash__(self):
        """Compute the hash of a Node.

        Together with __eq__ allows putting Node objects in a set.
        """
        return hash(frozenset((self.left, self.right, self.root)))


class Trees:
    def __init__(self):
        """Initialize starting trees."""
        self.trees = [
            {Leaf()},  # n=1
            {Node(Leaf(), Leaf(), root=True)},  # n=2
            {Node(Node(Leaf(), Leaf()), Leaf(), root=True)},  # n=3
        ]

    def generate_trees(self, n):
        """Generate all rooted unlabeled binary trees with n leafs.

        The algorithm works as follows:
        1. If there are trees with n leafs in a list self.trees, just return it.
        2. Else, take the set of trees with highest number of leafs/
        3. In each tree replace each leaf with a node with two leafs as its children (so the tree has one more leaf).
        4. Add it to a set of trees with one more leaf.
        5. Repeat 2-4 until you have a set of trees with n leafs.
        """
        max_n = len(self.trees)
        if n > max_n:
            i = max_n
            while i <= n:
                i += 1
                trees_to_add = set()
                for tree in self.trees[-1]:
                    for elem in tree:
                        if elem.is_leaf:
                            continue
                        if elem.left.is_leaf:
                            elem.left = Node(Leaf(), Leaf())
                            trees_to_add.add(deepcopy(tree))
                            elem.left = Leaf()
                        if elem.right.is_leaf:
                            elem.right = Node(Leaf(), Leaf())
                            trees_to_add.add(deepcopy(tree))
                            elem.right = Leaf()
                self.trees.append(trees_to_add)
        return self.trees[n - 1]


if __name__ == "__main__":
    n = int(sys.argv[1])
    trees = Trees()
    if n == 1:
        print("();")
    else:
        for tree in trees.generate_trees(n):
            print(tree)
