#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def find_max_at_depth(root, depth):
    if not root:
        return None
    if depth == 0:
        return root.value

    queue = [(root, 0)] 
    max_value = float("-inf")

    while queue:
        node, current_depth = queue.pop(0)

        if current_depth == depth:
            max_value = max(max_value, node.value)

        if node.left:
            queue.append((node.left, current_depth + 1))
        if node.right:
            queue.append((node.right, current_depth + 1))

    return max_value if max_value != float("-inf") else None


if __name__ == "__main__":
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(7), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
    )
    limit = 2
    
    max_value = find_max_at_depth(root, limit)
    print(f"Максимальное значение на указанной глубине: {max_value}")
