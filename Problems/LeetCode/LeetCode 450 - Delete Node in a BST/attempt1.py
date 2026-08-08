# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftmost(self, root):
        if not root:
            return
        if not root.left:
            return root
        return self.leftmost(root.left)

    def successor(self, root, y):
        suc = None
        current = root
        while current:
            if current.val == y:
                suc = self.leftmost(current.right) if current.right else suc  
                break
        return suc
                     
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and root.right:
                z = self.successor(root, root.val) 
                root.val = z.val
                root.right = self.deleteNode(root.right, z.val)
            elif root.left or root.right:
                root = root.left if root.left else root.right
        return root                           
        