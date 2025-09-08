class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        self.prev = None
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        return inorder(root)

# Helper to build tree from list (level order)
def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

# Test cases
test_cases = [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([10, 5, 15, None, None, 6, 20], False)
]

solver = Solution()
for nodes, expected in test_cases:
    root = build_tree(nodes)
    result = solver.isValidBST(root)
    print(f"Input: {nodes} -> Output: {result}, Expected: {expected}")
