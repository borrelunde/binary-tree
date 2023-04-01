class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type: str):
        if traversal_type == "left_order":
            return self.order_left_print(tree.root, "")[:-1]
        elif traversal_type == "in_order":
            return self.in_order_print(tree.root, "")[:-1]
        elif traversal_type == "right_order":
            return self.order_right_print(tree.root, "")[:-1]
        elif traversal_type == "post_order":
            return self.post_order_print(tree.root, "")[:-1]

    def order_left_print(self, node: Node, traversal: str):
        """
        Root-Left-Right
        """
        if node:
            traversal += (str(node.value) + "-")
            traversal = self.order_left_print(node.left, traversal)
            traversal = self.order_left_print(node.right, traversal)
        return traversal

    def in_order_print(self, node: Node, traversal: str):
        """
        Left-Root-Right
        """
        if node:
            traversal = self.in_order_print(node.left, traversal)
            traversal += f'{str(node.value)}-'
            traversal = self.in_order_print(node.right, traversal)
        return traversal

    def order_right_print(self, node: Node, traversal: str):
        """
        Right-Root-Left
        """
        if node:
            traversal += f'{str(node.value)}-'
            traversal = self.order_right_print(node.right, traversal)
            traversal = self.order_right_print(node.left, traversal)
        return traversal

    def post_order_print(self, node: Node, traversal: str):
        """
        Left-Right-Root
        """
        if node:
            traversal = self.post_order_print(node.left, traversal)
            traversal = self.post_order_print(node.right, traversal)
            traversal += f'{str(node.value)}-'
        return traversal


# Tree structure:
#         1
#      /     \
#     2       3
#   /   \   /   \
#  4     5 6     7
#                 \
#                  8


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("left_order"))   # 1-2-4-5-3-6-7-8
print(tree.print_tree("in_order"))     # 4-2-5-1-6-3-7-8
print(tree.print_tree("right_order"))  # 1-3-7-8-6-2-5-4
print(tree.print_tree("post_order"))   # 4-5-2-6-8-7-3-1
