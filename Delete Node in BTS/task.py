# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        def find(node, key):
            if node is None:
                return
            if node.val > key:
                node.left = find(node.left, key)
            elif node.val < key:
                node.right = find(node.right, key)
            elif node.val == key:
                if not node.left and not node.right:
                    return
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                else:
                    succ = node.right
                    while succ.left:
                        succ = succ.left
                    node.val = succ.val
                    node.right = find(node.right, succ.val)
                    return node
            return node
        
        return find(root, key)

        


            


        
