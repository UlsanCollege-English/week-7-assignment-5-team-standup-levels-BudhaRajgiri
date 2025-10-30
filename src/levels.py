# levels.py

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """Return level order traversal (BFS) of a binary tree."""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


def zigzag_level_order(root):
    """Return zigzag (left-right, right-left) level order traversal."""
    if not root:
        return []
    res = []
    q = deque([root])
    left_to_right = True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
    return res


def right_side_view(root):
    """Return the rightmost node of each level (visible from right side)."""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        rightmost = None
        for _ in range(len(q)):
            node = q.popleft()
            rightmost = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(rightmost)
    return res
