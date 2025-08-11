from collections import deque
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_bst(root, min_val, max_val):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

def main()
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("true")
        return
    
    # Build tree from level order
    if tokens[0] != "None":
        root = TreeNode(int(tokens[0]))
    else:
        print("true")
        return
    
    q = deque([root])
    i = 1
    while q and i < len(tokens):
        node = q.popleft()
        
        # Left child
        if i < len(tokens) and tokens[i] != "None":
            node.left = TreeNode(int(tokens[i]))
            q.append(node.left)
        i += 1
        
        # Right child
        if i < len(tokens) and tokens[i] != "None":
            node.right = TreeNode(int(tokens[i]))
            q.append(node.right)
        i += 1
    
    print("true" if is_valid_bst(root, float('-inf'), float('inf')) else "false")

if __name__ == "__main__":
    main()